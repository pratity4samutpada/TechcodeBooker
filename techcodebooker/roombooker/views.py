from django.shortcuts import render
from .forms import room_form, booking_form, confirm_booking
from formtools.wizard.views import SessionWizardView, WizardView

# Create your views here.

def index(request):
    return render(request,'roombooker/roomselection.html',{'form':room_form})

def book(request):
    return render(request, 'roombooker/booking.html',{'form':booking_form})

def confirmation(request):
    return render(request, 'roombooker/confirmation.html',{})

FORMS = [
    ("Rooms", room_form),
    ("Booking", booking_form),
    ("Confirm", confirm_booking)
]

TEMPLATES = {"Rooms":"roombooker/roomselection.html",
             "Booking":"roombooker/booking.html",
             "Confirmation":"roombooker/confirmation.html"
             }

class BookingWizard(SessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render('roombooker/done.html',{})