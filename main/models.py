from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .choices import *
# Create your models here.


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userType = models.IntegerField(choices=USER_TYPE, default=2)

    def __str__(self) -> str:
        return self.user.username + " - " + self.userType

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilePhoto = models.ImageField(upload_to="profile_photos")
    location = models.TextField(max_length=100) # TODO actual location from google.
    
    def __str__(self) -> str:
        return self.user.username + "'s profile"



class Studio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    location = models.TextField(max_length=100) # TODO actual location from google.


class StudioMedia(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    media = models.FileField(upload_to="studio_photos")

class BookingSession(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)
    bookedByUser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    status = models.IntegerField(choices=BOOKING_STATUS_CHOICES)
    
    bookingDate = models.DateTimeField(default=datetime.now())   # when the booking was done. value needs to be time.now       
    startTime = models.DateTimeField(default=datetime.now())    # start time of the slot
    endTime = models.DateTimeField(default=datetime.now())      #


# stores all the users in the Booking session. 
class BookingSessionUserRelation(models.Model):
    bookingSession = models.ForeignKey(BookingSession, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices= USER_STATUS_IN_BOOKING_SESSION)

class BookingSessionPayment(models.Model):
    bookingSession = models.ForeignKey(BookingSession, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.IntegerField(choices=PAYMENT_STATUS_CHOICES)
    paymentDateTime = models.DateTimeField(default=datetime.now())
    
    
class BookingSessionChat(models.Model):
    bookingSession = models.ForeignKey(BookingSession, on_delete=models.DO_NOTHING)
    sentByUser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    messageDatetime = models.DateTimeField(default=datetime.now())
    message = models.TextField(max_length=100000)
    

