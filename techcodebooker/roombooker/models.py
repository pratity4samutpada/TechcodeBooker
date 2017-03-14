from django.db import models
from django.utils import timezone
import datetime as dt

#Contains info about rooms. CM may upload images and modify fields or the list itself.
class Rooms (models.Model):
    room_name = models.CharField(max_length=200)
    room_image = models.ImageField(upload_to="roomimages")
    room_capacity = models.IntegerField()
    room_fac = models.CharField("Room Facilities",max_length=999)
    def __str__(self):
       return self.room_name

#List of all the companies that can book a room.
class Companies (models.Model):
    company_name = models.CharField(max_length=200)
    def __str__(self):
        return self.company_name

#Each Bookings object should be unique.
class Bookings (models.Model):

        def combine_dt(self,date,time):
           return dt.datetime.combine(date,time)

        room = models.ForeignKey('Rooms', on_delete=models.CASCADE)
        start_time = models.IntegerField("From")
        start_minutes = models.FloatField("Start minute.",default=0)
        end_time = models.IntegerField("To")
        end_minutes = models.FloatField("End Minutes",default=0)
        date = models.DateField("Date", default=timezone.now)
        booking_time = models.DateField("Time the booking was made",auto_now_add=True)
        company = models.ForeignKey('Companies',on_delete=models.CASCADE)
        email = models.EmailField('Your Email')
        booked_by = models.CharField('Full Name', max_length=50)
        status=models.BooleanField('Pending',default=False)


        def __str__(self):
            return "Booking from: "+str(self.start_time)+" to "+str(self.end_time)



#We might have to make a seperate model that holds a list of every object's start_datetime and end_datetime that allows us
#to work with ranges. Right now, we only have start and end info, so if someone books 2-4, we have 2, we have 4, but
#we also need 3 so that the calendar fills out correctly. We could just say that start and end-1 will be blocked out,
#but what if it's the case that someone is approved for > 2 hours of booking. 3-7?
