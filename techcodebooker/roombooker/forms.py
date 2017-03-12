from django import forms
from .models import Bookings, Companies, Rooms
from django.utils.html import conditional_escape, mark_safe
from django.forms.extras.widgets import SelectDateWidget
import datetime



class room_form(forms.Form):
    room_id = forms.IntegerField(min_value=0,widget=forms.HiddenInput())

class booking_form(forms.Form):
    company= forms.ModelChoiceField(queryset=Companies.objects.all(),empty_label="Company")
    email = forms.EmailField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    booked_by = forms.CharField(max_length=200,widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    booking_date = forms.DateField(initial=datetime.date.today, widget=SelectDateWidget(attrs={'class':'book-date'}))
    start_time = forms.ChoiceField(choices=((i,str(i)+':00') for i in range(24)), widget=forms.Select())
    end_time = forms.ChoiceField(choices=((i,str(i)+':00') for i in range(24)), widget=forms.Select())
    status = forms.BooleanField(initial=False,widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(booking_form, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['company'].label=""
        self.fields['booked_by'].label=""

    def clean_booking_date(self):
        date = self.cleaned_data['booking_date']
        thirty_days_after = datetime.date.today() + datetime.timedelta(days=30)
        if date > thirty_days_after:
            raise forms.ValidationError("Cannot reserve a room more than 30 days in advance.")
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date


class confirm_booking(forms.Form):
    status = forms.CharField(initial="confirmed", widget=forms.HiddenInput())

