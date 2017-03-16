from .models import Rooms, Bookings,Companies
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core import serializers

def dashboard(request):
    rooms = Rooms.objects.all()
    bookings = Bookings.objects.all().order_by('-date')
    companies = Companies.objects.all()
    context = {'rooms':rooms,'bookings':bookings,'companies':companies}
    return render(request,'communitymanager/dashboard.html',context)

def bookings_dash(request):
    bookings = Bookings.objects.all()
    context={'bookings':bookings}
    return render(request,'communitymanager/bookings_dash.html',context)