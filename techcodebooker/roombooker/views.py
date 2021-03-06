from .forms import room_form, booking_form, confirm_booking
from formtools.wizard.views import SessionWizardView
from .models import Rooms, Bookings, Companies
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json, datetime
from django.core import serializers
from django.core.mail import send_mail

# The forms for BookingWizard.
FORMS = [
    ("Rooms", room_form),
    ("Booking", booking_form),
    ("Confirm", confirm_booking)
]

# Templates for BookingWizard.
TEMPLATES = {"Rooms": "roombooker/roomselection.html",
             "Booking": "roombooker/booking.html",
             "Confirm": "roombooker/confirmation.html",
             "Done": "roombooker/done.html"
             }


# Booking Wizard gives you three forms, when they're all filled out, it invokes done(). By modifying .done(), we can retrieve
# the form info and save it to the  db.
class BookingWizard(SessionWizardView):
    # For iterating over the array of template names.
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    # This makes the Rooms model a data-attribute of our Wizard. This gives the form/wizard access to all the data under this model from the form.
    def rooms(self):
        return Rooms.objects.all()

    # Grabs info from previous form inputs for use in later form steps.
    def get_context_data(self, form, **kwargs):
        context = super(BookingWizard, self).get_context_data(form=form, **kwargs)
        new_context = {}

        if self.steps.step1 == 2 or self.steps.step1 == 3:
            id = self.get_cleaned_data_for_step('Rooms')['room_id']
            room = Rooms.objects.get(pk=id)
            new_context['data_from_step_1'] = room
            if self.steps.step1 == 3:
                booking = self.get_cleaned_data_for_step('Booking')
                new_context['start_minutes'] = str(int(float(booking['start_minutes']) * 60)).zfill(2)
                new_context['end_minutes'] = str(int(float(booking['end_minutes']) * 60)).zfill(2)
                new_context['data_from_step_2'] = booking
                if booking['status'] == 'pending':
                    new_context['message'] = {
                        'msg': "Your reservation is longer than two hours and will be pending approval. An email will be sent to the Community Manager."}
                else:
                    new_context['message'] = {
                        'msg': "An email with reservation details will be sent to the address you provided."}
            context.update(new_context)
        return context

    # For saving form data to the db in a Bookings object.
    def newBookingObject(self, room, booking, status):
        r, b, s = room, booking, status
        r_obj = Rooms.objects.get(pk=r['room_id'])
        status_bool = False

        # In case the user waited too long on the confirmation page or their time was booked during the booking process.
        bookings_on_d = Bookings.objects.filter(date=b['booking_date'], room=int(r['room_id']))
        if is_conflict(bookings_on_d ,b['start_time'],b['start_minutes'],b['end_time'],b['end_minutes']):
            return False

        if b['status'] == 'pending':
            status_bool = True
        try:
            newBooking = Bookings(room=r_obj, start_time=b['start_time'], start_minutes=b['start_minutes'],
                                  end_time=b['end_time'], end_minutes=b['end_minutes'],
                                  date=b['booking_date'],
                                  company=b['company'], note=b['note'], email=b['email'], booked_by=b['booked_by'], status=status_bool)

            newBooking.save()
            print(newBooking.note)
            return True
        except:
            return False

    # This is the method that is invoked when all the forms have been completed by the user.
    # form_list is the list of objects containing the user's form information.
    def done(self, form_list, **kwargs):

        form_data = [form.cleaned_data for form in form_list]
        room = form_data[0]
        booking = form_data[1]
        status = form_data[2]
        context = {
            'form_data': [form.cleaned_data for form in form_list],
        }

        # If newBookingObject returns False, it means something went wrong updating the db, so it just adds an error msg to the context.
        if not self.newBookingObject(room, booking, status):
            context['error'] = 'There was a problem adding the data to the database. Please try again.'
        elif not send_email(room,booking,status):
            context['error'] = 'There was a problem sending the email.'

        return render_to_response('roombooker/done.html', context)


# SERVICES HANDLING AJAX REQUESTS WITHIN SPECIFIC FORM STEPS.
# Retrieves the data about each room and sends it to ajax callback.
def get_room_info(request):
    id = request.GET.get('id')
    room = []
    room.append(Rooms.objects.get(pk=id))
    result = serializers.serialize('json', room, fields=('room_name', 'room_capacity', 'room_fac', 'room_notes'))
    return HttpResponse(result, content_type='application/json')


# Gets time info & room info from form and checks whether or not the time is available for that room.
def validate_time(request):
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    s_minute = float(request.GET.get('s_minute'))
    e_minute = float(request.GET.get('e_minute'))
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    room = request.GET.get('room')
    d = datetime.date(int(year), int(month), int(day))

    bookings_on_d = Bookings.objects.filter(date=d, room=int(room))
    context = {}
    if (start+s_minute) >= (end+e_minute):
        context['error'] = 'Not a valid booking time.'
    elif is_conflict(bookings_on_d, start,s_minute, end, e_minute):
        context['error'] = 'Cannot reserve room for time that is already booked.'
    elif gt_2_hours(start,s_minute,end,e_minute):
        context['pending'] = 'Reservations longer than two hours require community manager approval.'
    else:
        context['success'] = 'This time slot is currently available.'
    return HttpResponse(json.dumps(context), content_type="application/json")


# Handles different cases of overlapping times.
def is_conflict(bookings, start, s_minute,end,e_minute):
    v_start = start + s_minute
    v_end = end + e_minute
    for booking in bookings:
        st = booking.start_time + booking.start_minutes
        et = booking.end_time + booking.end_minutes
        if st == v_start:
            return True
        if (st > v_start) & (v_end > st):
            return True
        if (et > v_start) & (et < v_end):
            return True
        if (st < v_start) & (et >= v_end):
            return True
    return False


def gt_2_hours(start,s_minute, end, e_minute):
    v_start = start + s_minute
    v_end = end + e_minute
    return (v_end - v_start) > 2

def send_email(room,booking,status):
    try:
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
            )
        return True
    except:
        return False