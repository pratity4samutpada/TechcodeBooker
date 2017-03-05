from django.shortcuts import render
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,'roombooker/roomselection.html',{})

def book(request):
    return render(request, 'roombooker/booking.html',{'form':BookingForm()})

def confirmation(request):
    return render(request, 'roombooker/confirmation/html',{})