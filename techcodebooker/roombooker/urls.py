from django.conf.urls import url
from .views import BookingWizard, FORMS
from . import views,views_dash,views_calendar
from django.contrib.auth import views as authviews


urlpatterns = [
    url(r'^$', BookingWizard.as_view(FORMS)),
    url(r'^dashboard$', views_dash.index, name='dashboard'),
    url(r'^dashboard/rooms$', views_dash.rooms,name='rooms'),
    url(r'^dashboard/companies$',views_dash.companies,name='companies'),
    url(r'^dashboard/bookings$',views_dash.bookings,name='bookings'),
    url(r'^pendingaction$',views_dash.pendingaction,name='pendingaction'),
    url(r'^getroominfo$', views.get_room_info, name='getroominfo'),
    url(r'^validatetime$', views.validate_time, name='validatetime'),
    url(r'^populatecal$',views_calendar.populate, name='populatecal'),
    url(r'^login$', authviews.login ,name='login'),
    url(r'^logout$', authviews.logout, {'next_page': '/booker'}, name='logout'),


]