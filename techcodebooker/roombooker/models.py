from django.db import models
from django.forms import ModelForm
from django.utils import timezone
# Create your models here.

class Rooms (models.Model):
    room_name = models.CharField(max_length=200)
    room_image = models.ImageField(upload_to="roomimages")
    room_capacity = models.IntegerField()
    room_fac = models.CharField("Room Facilities",max_length=999)
    def __str__(self):
       return self.room_name

class Companies (models.Model):
    company_name = models.CharField(max_length=200)
    def __str__(self):
        return self.company_name


class Bookings (models.Model):
        room = models.ForeignKey('Rooms', on_delete=models.CASCADE)
        start_time = models.TimeField("From")
        end_time = models.TimeField("To")
        date = models.DateField("Date", default=timezone.now)
        booking_time = models.DateField("Time the booking was made",auto_now_add=True)
        company = models.ForeignKey('Companies',on_delete=models.CASCADE)
        email = models.EmailField('Your Email')
        booked_by = models.CharField('Full Name', max_length=50)
        status=models.BooleanField('Pending',default=False)


        def __str__(self):
            return "Booking from: "+str(self.start_time)+" to "+str(self.end_time)
        # status = models.CharField()

        # def set_status(self): if total time booked > 2 hours, will set the status to pending + send email to CM.
        # Else will set status to confirmed
        # CM will be able to change status- either to confirmed or to delete the booking altogether.


