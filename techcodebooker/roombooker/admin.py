from django.contrib import admin
from .models import Companies, Bookings, Rooms
from django.conf.urls import url
from django.http import HttpResponse

# Register your models here.

admin.site.register(Bookings)
admin.site.register(Companies)
admin.site.register(Rooms)
