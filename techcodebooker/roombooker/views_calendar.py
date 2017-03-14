import json, datetime
from django.core import serializers
from django.http import HttpResponse

from .models import Bookings

def populate(request):
    id = request.GET.get('id')
    result={}
    current_date = datetime.date.today()
    max_date = current_date + datetime.timedelta(days=30)
    bookings_for_r = Bookings.objects.filter(room__pk=id, date__gte=current_date, date__lte=max_date)
    event_list = map_event_list(bookings_for_r)
    result["events"]=event_list
    return HttpResponse(json.dumps(result),content_type='application/json')

def map_event_list(bookings):
    event_list = []
    for booking in bookings:
            newObj = {}
            newObj['id']=booking.id
            newObj['start']="{0}T{1}:00:00.000".format(booking.date.strftime("%Y-%m-%d"),str(booking.start_time).zfill(2))
            newObj['end']="{0}T{1}:00:00.000".format(booking.date.strftime("%Y-%m-%d"),str(booking.end_time).zfill(2))
            newObj['title']='Reserved'
            print(newObj)
            event_list.append(newObj)
    return event_list


