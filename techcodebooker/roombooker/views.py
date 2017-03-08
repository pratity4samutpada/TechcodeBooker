from django.shortcuts import render
from .forms import room_form, booking_form, confirm_booking
from formtools.wizard.views import SessionWizardView
from .models import Rooms, Bookings
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
from django.core import serializers

FORMS = [
    ("Rooms", room_form),
    ("Booking", booking_form),
    ("Confirm", confirm_booking)
]

TEMPLATES = {"Rooms": "roombooker/roomselection.html",
             "Booking": "roombooker/booking.html",
             "Confirm": "roombooker/confirmation.html",
             "Done": "roombooker/done.html"
             }


class BookingWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def rooms(self):
        return Rooms.objects.all()

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

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        room = form_data[0]
        booking = form_data[1]
        status = form_data[2]
        context = {
            'form_data': [form.cleaned_data for form in form_list],
        }

        if not self.newBookingObject(room, booking, status):
            context['error'] = 'There was a problem adding the data to the database.'

        return render_to_response('roombooker/done.html', context)


def get_room_info(request):
    id = request.GET.get('id')
    room = Rooms.objects.get(pk=id)
    result = serializers.serialize('json', [room], fields=('room_name','room_capacity','room_fac'))
    return HttpResponse(result,content_type='application/json')
