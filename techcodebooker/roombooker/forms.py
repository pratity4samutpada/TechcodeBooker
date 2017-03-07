from django import forms
from .models import Bookings, Companies, Rooms
from django.utils.html import conditional_escape, mark_safe
from django.forms.extras.widgets import SelectDateWidget



# class BookingForm (forms.ModelForm):
#     company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Company Name")
#     class Meta:
#         model = Bookings
#         fields = ['company','booked_by','email','start_time','end_time','room']


class room_form(forms.Form):
    room_id = forms.IntegerField(min_value=0,widget=forms.HiddenInput())

class booking_form(forms.Form):
    company= forms.ModelChoiceField(queryset=Companies.objects.all())
    email = forms.EmailField()
    booked_by = forms.CharField(max_length=200)
    day_of_booking = forms.DateField(widget=SelectDateWidget())
    start_time = forms.TimeField()
    end_time = forms.TimeField()

class confirm_booking(forms.Form):
    status = forms.CharField(initial="confirmed", widget=forms.HiddenInput())

