from django import forms
from .models import Bookings, Companies


class BookingForm (forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label=None)
    class Meta:
        model = Bookings
        fields = ['start_time','end_time','company','room','email','booked_by']