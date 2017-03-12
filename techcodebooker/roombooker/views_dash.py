from .models import Rooms, Bookings
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core import serializers

def dashboard(request):
    rooms = Rooms.objects.all()
    bookings = Bookings.objects.all().order_by('-date')
    context = {'rooms':rooms,'bookings':bookings}
    return render(request,'communitymanager/dashboard.html',context)