from django.conf.urls import url
from .views import BookingWizard, FORMS
from . import views,views_dash,views_calendar
from django.contrib.auth import views as authviews


urlpatterns = [
    url(r'^$', BookingWizard.as_view(FORMS)),
    url(r'^dashboard$', views_dash.dashboard, name='dashboard'),
    url(r'^getroominfo$', views.get_room_info, name='getroominfo'),
    url(r'^validatetime$', views.validate_time, name='validatetime'),
    url(r'^populatecal$',views_calendar.populate, name='populatecal'),
    url(r'^bookingsdash$',views_dash.bookings_dash, name='bookingsdash'),
    url(r'^login$', authviews.login ,name='login'),
    url(r'^logout$', authviews.logout, {'next_page': '/booker'}, name='logout'),

]