from django.conf import settings
from django.conf.urls import url
from .views import viewRefugees, viewRefugeeCamp, placeRefugeeCamp, home_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^view/', viewRefugees, name='view'),
    url(r'^camps/', viewRefugeeCamp, name='camps'),
    url(r'^place/', placeRefugeeCamp, name='place'),
]
