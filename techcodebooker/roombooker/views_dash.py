from .models import Rooms, Bookings,Companies
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core import serializers

def index(request):
    bookings = Bookings.objects.filter(status=True).order_by('-date')
    context = {'bookings':bookings}
    return render(request,'communitymanager/index.html',context)

def bookings(request):
    bookings = Bookings.objects.all().order_by('-date')
    context={'bookings':bookings}
    return render(request,'communitymanager/bookings.html',context)

def rooms(request):
    rooms = Rooms.objects.all()
    context={'rooms':rooms}
    return render(request, 'communitymanager/rooms.html',context)

def companies(request):
    companies = Companies.objects.all()
    context = {'companies':companies}
    return render(request, 'communitymanager/companies.html',context)

def pendingaction(request):
    action = request.GET.get('action')
    id = int(request.GET.get('id'))
    booking = Bookings.objects.get(pk=id)
    msg ={}
    if action == 'delete':
        booking.delete()
        msg['msg']="Pending booking was deleted."
    else:
        booking.status=False
        booking.save()
        msg['msg']="Pending booking was approved."
    return HttpResponse(json.dumps(msg),content_type='application/json')

def edit_company(request,id):
    instance = Companies.objects.get(pk=id)
    return render(request,'communitymanager/edit_company.html',{'instance':instance})
