from .models import Rooms, Bookings
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
import json
from django.core import serializers

def dashboard(request):

    return render(request,'communitymanager/dashboard.html',{})