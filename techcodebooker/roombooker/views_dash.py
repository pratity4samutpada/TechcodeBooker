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
    return render(request,'communitymanager/main.html',context)

def switch_view(request):
    template_name = request.GET.get('template')
    template_path = "communitymanager/{}.html".format(template_name)
    return render(request,template_path)