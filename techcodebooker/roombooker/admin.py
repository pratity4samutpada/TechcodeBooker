from django.contrib import admin
from .models import Companies, Bookings, Rooms
from django.conf.urls import url
from django.http import HttpResponse

# Register your models here.


class MyModelAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super(MyModelAdmin, self).get_urls()
        my_urls = [
            url(r'^/approve$', self.admin_site.admin_view(self.approve)),
        ]
        return my_urls + urls

    def approve(request):
        id = request.POST.get('id')
        booking = Bookings.objects.get(pk=int(id))
        booking.status = False
        booking.save()
        msg = "Booking on {0} from {1} to {2} approved.".format(booking.date.strftime("%Y-%m-%d"),
                                                            booking.whole_start_time, booking.whole_end_time)
        context = {'msg': msg}
        return HttpResponse(context)



admin.site.register(Bookings,MyModelAdmin)
admin.site.register(Companies)
admin.site.register(Rooms)
