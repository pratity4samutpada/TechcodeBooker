from django.shortcuts import render
from .forms import room_form, booking_form, confirm_booking
from formtools.wizard.views import SessionWizardView
from .models import Rooms, Bookings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.core import serializers

# The forms for BookingWizard.
FORMS = [
    ("Rooms", room_form),
    ("Booking", booking_form),
    ("Confirm", confirm_booking)
]

#Templates for BookingWizard.
TEMPLATES = {"Rooms": "roombooker/roomselection.html",
             "Booking": "roombooker/booking.html",
             "Confirm": "roombooker/confirmation.html",
             "Done": "roombooker/done.html"
             }

# Booking Wizard gives you three forms, when they're all filled out, it invokes done(). By modifying .done(), we can retrieve
#the form info and save it to the  db.
class BookingWizard(SessionWizardView):

    #For iterating over the array of template names.
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    #This makes the Rooms model a data-attribute of our Wizard. This gives the form/wizard access to all the data under this model from the form.
    def rooms(self):
        return Rooms.objects.all()

    #For saving form data to the db in a Bookings object.
    def newBookingObject(self, room, booking, status):
        r, b, s = room, booking, status
        r_obj = Rooms.objects.get(pk=r['room_id'])

        if s['status'] == 'confirmed':
            statusBool = False

            try:
                newBooking = Bookings(room=r_obj, start_time=b['start_time'], end_time=b['end_time'],
                                  date=b['booking_date'],
                                  company=b['company'], email=b['email'], booked_by=b['booked_by'], status=statusBool)
                newBooking.save()
                return True
            except:
                return False

    #This is the method that is invoked when all the forms have been completed by the user.
    #form_list is the list of objects containing the user's form information.
    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        room = form_data[0]
        booking = form_data[1]
        status = form_data[2]
        context = {
            'form_data': [form.cleaned_data for form in form_list],
        }

        #If newBookingObject returns False, it means something went wrong updating the db, so it just adds an error msg to the context.
        if not self.newBookingObject(room, booking, status):
            context['error'] = 'There was a problem adding the data to the database.'

        return render_to_response('roombooker/done.html', context)

#Retrieves the data about each room and sends it to ajax callback.
def get_room_info(request):
    id = request.GET.get('id')
    room = []
    room.append(Rooms.objects.get(pk=id))
    result = serializers.serialize('json', room, fields=('room_name','room_capacity','room_fac'))
    return HttpResponse(result,content_type='application/json')
