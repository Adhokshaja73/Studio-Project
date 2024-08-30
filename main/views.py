from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Check login -> if not redirect to login.
# If logged in. 
def home(request):
    return(HttpResponse("Hi"))

# shows homepage to user. decide content and then code
def userHome(request):
    pass


# shows homepage for studio owners. Decide content and code
def studioUserHome(request):
    pass


# create profiles for all users
def createProfile(request):
    pass

# update profile for all users
def updateProfile(request):
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

