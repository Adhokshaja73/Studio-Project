from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .choices import *
from django.core.validators import MinLengthValidator
# Create your models here.


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userType = models.IntegerField(choices=USER_TYPE, default=2)

    def __str__(self) -> str:
        return self.user.username + " - " + self.userType.__str__()

class Studio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    email = models.EmailField(max_length=1000)
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    location = models.TextField(max_length=100) # TODO actual location from google.
    city = models.TextField(max_length=100) # TODO actual location from google.
    
    # not mandatory fileds
    description = models.TextField(max_length=1000) 
    iconUrl = models.TextField(max_length=1000)

    # admin added.
    verificationStatus = models.IntegerField(choices=VERIFICATION_STATUS, default=1)

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)

    location = models.TextField(max_length=100) # TODO actual location from google.
    profilePicUrl =  models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return self.user.username + "'s profile"
    
class CalendarItem(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)
    bookedByUser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    status = models.IntegerField(choices=BOOKING_STATUS_CHOICES)
    
    bookingDate = models.DateTimeField(default=datetime.now())   # when the booking was done. value needs to be time.now       
    startTime = models.DateTimeField(default=datetime.now())    # start time of the slot
    endTime = models.DateTimeField(default=datetime.now())      #

class StudioMedia(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    media = models.FileField(upload_to="studio_photos")



# stores all the users in the Booking session. 
class BookingSessionUserRelation(models.Model):
    calendarItem = models.ForeignKey(CalendarItem, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices= USER_STATUS_IN_BOOKING_SESSION)

class BookingSessionPayment(models.Model):
    calendarItem = models.ForeignKey(CalendarItem, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.IntegerField(choices=PAYMENT_STATUS_CHOICES)
    paymentDateTime = models.DateTimeField(default=datetime.now())
    
    
class BookingSessionChat(models.Model):
    calendarItem = models.ForeignKey(CalendarItem, on_delete=models.DO_NOTHING)
    sentByUser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    messageDatetime = models.DateTimeField(default=datetime.now())
    message = models.TextField(max_length=100000)
    

