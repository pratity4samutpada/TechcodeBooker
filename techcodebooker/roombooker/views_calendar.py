import json, datetime
from django.http import HttpResponse
from .models import Bookings

# Handles an ajax request. Requests sent from the community manager page come with dash_id.
# Retrieves all bookings for the given room id, returns the parsed bookings entries to the calendar plugin.
def populate(request, dash_id=None):
    result = {}
    current_date = datetime.date.today()
    max_date = current_date + datetime.timedelta(days=30)
    id = request.GET.get('id')
    bookings_for_r = Bookings.objects.filter(room__pk=id, date__gte=current_date, date__lte=max_date)
    event_list = map_event_list(bookings_for_r, dash_id)
    result["events"] = event_list
    return HttpResponse(json.dumps(result), content_type='application/json')

# Parses DB to plugin-readable format.
def map_event_list(bookings, dash_id=None):
    event_list = []
    for booking in bookings:
        s_min = str(int(booking.start_minutes * 60)).zfill(2)
        e_min = str(int(booking.end_minutes * 60)).zfill(2)
        newObj = {}
        newObj['id'] = booking.id
        newObj['start'] = "{0}T{1}:{2}:00.000".format(booking.date.strftime("%Y-%m-%d"),
                                                      str(booking.start_time).zfill(2), s_min)
        newObj['end'] = "{0}T{1}:{2}:00.000".format(booking.date.strftime("%Y-%m-%d"), str(booking.end_time).zfill(2),
                                                    e_min)
        if dash_id:
            newObj['title'] = booking.company.company_name
        else:
            newObj['title'] = 'Reserved'
        event_list.append(newObj)
    return event_list
