from django.contrib import admin
from .models import Companies, Bookings, Rooms
# Register your models here.

class MyAdminSite(admin.AdminSite):
    pass


admin.site.register(Companies)
admin.site.register(Bookings)
admin.site.register(Rooms)