from django.contrib import admin
from .models import Companies, Bookings, Rooms
from django.conf.urls import url
from django.http import HttpResponse

# Register your models here.

class BookingsAdmin(admin.ModelAdmin):
    list_display = ('room','company','date','whole_start_time','whole_end_time',)

admin.site.register(Bookings,BookingsAdmin)
admin.site.register(Companies)
admin.site.register(Rooms)
