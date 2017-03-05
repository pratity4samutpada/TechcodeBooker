from django import forms
from .models import Bookings, Companies


class BookingForm (forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Company Name")
    class Meta:
        model = Bookings
        fields = ['company','booked_by','email','start_time','end_time','room']