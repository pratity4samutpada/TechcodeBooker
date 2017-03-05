from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book$',views.book, name='book'),
    url(r'^confirmation$',views.confirmation, name='confirmation')
]