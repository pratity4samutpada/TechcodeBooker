from django.conf.urls import url
from .views import BookingWizard, FORMS
from . import views


urlpatterns = [
    url(r'^$', BookingWizard.as_view(FORMS)),
]