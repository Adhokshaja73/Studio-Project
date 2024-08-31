from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


# Check login -> if not redirect to login.
# If logged in. 
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
            return(render(request,'user_home.html'))
        # redirect to user home
        elif(userType.userType == 2):
            return(render(request,'studio_home.html'))
    else:
        # redirect to sign up page
        return(render(request,'user_profile_registration.html'))


# accepts post request only returns JSON. Handle the redirect in HTML.
# handle the arguments correctly to avoid any spam.
@login_required
def createStudioProfile(request):

    # reject if userprofile already exists
    # requests must have the following in the data. else error will be returned
    dataList = ['studio_name', 'studio_phone', 'studio_email', 'studio_image', 'csrfmiddlewaretoken']

    print(request.POST)
    if(request.method != "POST"):
        return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Only Post requests allowed'}}))
    elif(Studio.objects.filter(user = request.user).exists()):
       return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Studio profile for user already exits. please call to update'}}))
    elif(list(request.POST.keys()) != dataList):
        return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Invalid arguments'}}))
    else:
       return(JsonResponse({'status' : 'error', 'data' : {'message' : 'Invalid arguments'}}))
# accepts post request only returns JSON. Handle the redirect in HTML.
def createUserProfile(request):
    pass


# returns calendar with all bookings within select date range. 
def showStudioCalendar(request):
    pass

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

# retunrs list of all studios in the select city
def listStudios(request):
    pass

# returns list of all facilities in a studio
def getStudioFacilities(request):
    pass

# helps update the facilites.  
def updateFacilities(request):
    pass

