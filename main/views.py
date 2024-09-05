from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings as conf_settings

from base64 import b64decode
import os
# Create your views here.

 
#-------------------------------------------------------------------------------------------------------------------------------
#   RETURNS webpages 
#-------------------------------------------------------------------------------------------------------------------------------
@login_required 
def home(request):
    # check if user type is registered. If not redirect to page where you can setup. 
    # Ask if own a studio. If so, then redirect to the page.
    # Else just continue to the same userHomePage. 
    userType = UserType.objects.filter(user = request.user)
    if(userType.exists() == True):
        userType = userType.get()
        # redirect to studio home
        if(userType.userType == 1):
            return(render(request,'studio_home.html'))
        # redirect to user home
        elif(userType.userType == 2):
            return(render(request,'user_home.html'))
    else:
        # redirect to sign up page
        return(render(request,'user_profile_registration.html'))


# accepts post request only returns JSON. Handle the redirect in HTML.
# handle the arguments correctly to avoid any spam.
# argumentlists required : 
#-------------------------------------------------------------------------------------------------------------------------------
#   name                    type     required      description
#-------------------------------------------------------------------------------------------------------------------------------
#  studio_name              str       yes           Name : Will be displayed to all users
#  studio_phone             str       yes           Phone number of studio
#  studio_email             str       yes           Business email of the studio
#  studio_location          str       yes           Location of the studio
#  studio_image             image     no            Icon for the studio. 
#  studio_desc              str       no            Description of the studio. Free text
# _______________________________________________________________________________________________________________________________
#   RETURNS : JSON OBEJCT
# _______________________________________________________________________________________________________________________________
@login_required
def createStudioProfile(request):

    # reject if userprofile already exists
    # requests must have the following in the data. else error will be returned
    dataList = set(['studio_name', 'studio_phone', 'studio_email', 'studio_location','csrfmiddlewaretoken'])
    imagePath = ""

    if(request.method != "POST"):
        # only post requests allowed
        return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Only Post requests allowed'}}))
    
    elif(Studio.objects.filter(user = request.user).exists() or UserType.objects.filter(user = request.user).exists()):
       # blocks if user already has a profile
       return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Studio profile for already exits or user type is alredy defined. please call to update'}}))
    
    elif(dataList.issubset(set(request.POST.keys())) == False):
        # checks for mandatory fields in the request
        return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Invalid arguments'}}))
    
    else:
       
       # put mandatory fields into the model
        newStudio = Studio()
        newStudio.user = request.user
        newStudio.name = request.POST['studio_name']
        newStudio.email = request.POST['studio_email']
        newStudio.phone_number = request.POST['studio_phone']  
        newStudio.location = request.POST['studio_location']  

        # non mandatory fields
        newStudioDesc = ""
        newStudioImageUrl = ""

        try:
            # image data
            data_uri = request.POST["studio_image"]
            header, encoded = data_uri.split(",", 1)
            data = b64decode(encoded)
            imagePath = os.path.join(str(conf_settings.MEDIA_ROOT), "profile_photos" ,request.user.username + ".jpg" ) 
            with open(imagePath, "wb") as f:
                f.write(data)
            newStudioImageUrl = os.path.join(str(conf_settings.MEDIA_URL), "profile_photos" ,request.user.username + ".jpg" ).replace('\\','/')
        except Exception as e:
           pass
           
        try:
            # description   
            newStudioDesc = request.POST['studio_desc']
        except Exception as e:
           pass
        
        # save the new studio
        newStudio.description = newStudioDesc
        newStudio.iconUrl = newStudioImageUrl

        try:
            newStudio.save() # saves into DB
            newUserType = UserType(user = request.user, userType = 1)
            newUserType.save()

            return(JsonResponse({'status' : 'success', 'data' : {'message' : 'successfully created studio user and created user type', 'next_url' : '/'}}))
        except Exception as e:
            return(JsonResponse({'status' : 'error', 'data' : {'message' : e.__str__()}}))
        # create userType 

# accepts post request only returns JSON. Handle the redirect in HTML.
# handle the arguments correctly to avoid any spam.
# argumentlists required : 
#-------------------------------------------------------------------------------------------------------------------------------
#   name                    type     required      description
#-------------------------------------------------------------------------------------------------------------------------------
#   user_name               str      yes           name of the user 
#   user_image              image    no            Profile photo for the user 
#   user_location           str      no            Location of the user
#_______________________________________________________________________________________________________________________________
#
#   RETURNS : JSON OBEJCT   {status : val , data : {message : val , next_url : val }}
# ______________________________________________________________________________________________________________________________
@login_required
def createUserProfile(request):
    dataList = set(['user_name'])
    if(request.method != "POST"):
        # only post requests allowed
        return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Only Post requests allowed'}}))
    
    elif(Profile.objects.filter(user = request.user).exists() or UserType.objects.filter(user = request.user).exists()):
       # blocks if user already has a profile
       return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Studio profile for already exits or user type is alredy defined. please call to update'}}))
    
    elif(dataList.issubset(set(request.POST.keys())) == False):
        # checks for mandatory fields in the request
        return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Invalid arguments'}}))
    
    else:
        # mandatory fields 
        newUserProfile = Profile()
        newUserProfile.name = request.POST['user_name']
        newUserProfile.user = request.user

        # optional\
        newProfilePicurl = ""
        newProfileLocation = ""

        try:
            # image data
            data_uri = request.POST["user_image"]
            header, encoded = data_uri.split(",", 1)
            data = b64decode(encoded)
            imagePath = os.path.join(str(conf_settings.MEDIA_ROOT), "profile_photos" ,request.user.username + ".jpg" ) 
            with open(imagePath, "wb") as f:
                f.write(data)
            newProfilePicurl = os.path.join(str(conf_settings.MEDIA_URL), "profile_photos" ,request.user.username + ".jpg" ).replace('\\','/')
        except Exception as e:
           pass
            # description
        try:
            newProfileLocation = request.POST['user_location']
        except Exception as e:
           pass
        
        newUserProfile.location = newProfileLocation
        newUserProfile.profilePicUrl = newProfilePicurl
        try:
            newUserProfile.save()
            newUserType = UserType(user = request.user, userType = 2)
            newUserType.save()
            return(JsonResponse({'status' : 'success', 'data' : {'message' : 'successfully created user profile and created user type', 'next_url' : '/'}}))
        except Exception as e:
            return(JsonResponse({'status' : 'error', 'data' : {'message' : e.__str__()}}))

# returns JSON response with list of all studios in the selected location. 
# ONLY GET requests allowed
# requires argument :
#-------------------------------------------------------------------------------------------------------------------------------
#   name                type           required             description
#-------------------------------------------------------------------------------------------------------------------------------
#   city                str            yes                  city to filter studios.
#_______________________________________________________________________________________________________________________________
#
#   RETURNS : JSON OBEJCT {status : val, data : {message : val ,  studio_lisr : [list of studios]} }
#
# ______________________________________________________________________________________________________________________________
# @login_required
def getStudioList(request):
    if(request.method != "GET"):
        return(JsonResponse({'status' : 'error', 'data' :{'message' : 'only get requests are allowed'}}))
    try:
        requestCity = request.GET['city']
        studioList = list(Studio.objects.filter(location=requestCity).values    ('user','name','phone_number','location','city'))
        return(JsonResponse({'status' : 'success', 'data' :{'message' : 'request success', 'studio_list' : studioList}}))
    except Exception as e:
        return(JsonResponse({'status' : 'error', 'data' : {'message' : e.__str__()}}))
        
# returns calendar with all confirmed bookings within select date range.
# works for all users. Returns data with no check
# ONLY GET requests allowed
# requires argument :
#-------------------------------------------------------------------------------------------------------------------------------
#   name                type           required             description
#-------------------------------------------------------------------------------------------------------------------------------
#   studio_id           int            yes                  studio id
#   start_date          str            yes                  start date time in format YYYY-MM-DD HH:MM:SS
#   end_date            str            yes                  end date time in format YYYY-MM-DD HH:MM:SS
#_______________________________________________________________________________________________________________________________
#
#   RETURNS : JSON OBEJCT   {status : val , data : {message : val , calendar_items : [list of calendar items ] }}
#_______________________________________________________________________________________________________________________________
# @login_required
def getStudioCalendarToUser(request):

    paramList = set(['studio_id', 'start_date', 'end_date'])

    if(request.method != "GET"):
        return(JsonResponse({'status' : 'error', 'data' :{'message' : 'only get requests are allowed'}}))
    if(paramList != set(request.POST.keys())):
       return(JsonResponse({'status' : 'error', 'data' :{'message' : 'Invalid Parameters'}}))
    try:
        reqStudioId = request.GET['studio_id']
        reqStartDate = request.GET['start_date'] 
        reqEndDate = request.GET['end_date'] 
        calendarItemList = list(CalendarItem.objects.filter(studio = reqStudioId,status = 1,startTime__range = [reqStartDate, reqEndDate]).values('studio', 'startTime', 'endTime'))
        return(JsonResponse({'status' : 'success', 'data' :{'message' : 'request success', 'calendar_items' : calendarItemList}}))
    except Exception as e:
        return(JsonResponse({'status' : 'error', 'data' : {'message' : e.__str__()}}))



# returns calendar with all bookings within select date range.
# ONLY GET requests allowed
# REQUIRES LOGIN AS A STUDIO OWNER
# requires argument :
#-------------------------------------------------------------------------------------------------------------------------------
#   name                type           required             description
#-------------------------------------------------------------------------------------------------------------------------------
#   start_date          str            yes                  start date time in format YYYY-MM-DD HH:MM:SS
#   end_date            str            yes                  end date time in format YYYY-MM-DD HH:MM:SS
#_______________________________________________________________________________________________________________________________
@login_required
def getStudioCalendarToOwner(request):
    paramList = set(['start_date', 'end_date'])

    if(request.method != "GET"):
        return(JsonResponse({'status' : 'error', 'data' :{'message' : 'only get requests are allowed'}}))
    if(paramList != set(request.GET.keys())):
       return(JsonResponse({'status' : 'error', 'data' :{'message' : 'Invalid Parameters'}}))
    
    userStudio = Studio.objects.filter(user = request.user)
    if(userStudio.exists() != True):
        return(JsonResponse({'status' : 'error', 'data' :{'message' : 'Logged in user is not a studio owner.'}}))

    try:
        userStudio = userStudio.get()
        reqStartDate = request.GET['start_date'] 
        reqEndDate = request.GET['end_date'] 
        calendarItemList = list(CalendarItem.objects.filter(studio = userStudio,status = 1,startTime__range = [reqStartDate, reqEndDate]).values( 'studio','bookedByUser', 'status', 'bookingDate', 'startTime', 'endTime'))
        print(calendarItemList)
        return(JsonResponse({'status' : 'success', 'data' :{'message' : 'request success', 'calendar_items' : calendarItemList}}))
    except Exception as e:
        return(JsonResponse({'status' : 'error', 'data' : {'message' : e.__str__()}}))

# creates a booking event
def createBooking(request):
    pass

# cancels a booked event
def cancelBooking(request):
    pass

# updates a booked event
def updateBooking(request):
    pass

# returns all bookings made by a user. 
def getUserBookings(request):
    pass

# returns list of all facilities in a studio
def getStudioFacilities(request):
    pass

# helps update the facilites.  
def updateFacilities(request):
    pass

