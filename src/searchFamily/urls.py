from django.conf import settings
from django.conf.urls import url
from .views import FamilyListView, FamilyDetailView, addMember, familyMap, donate, adddonate
from ngo.views import viewRefugees, viewRefugeeCamp, placeRefugeeCamp, home_page

urlpatterns = [
    url(r'^detail/(?P<slug>[\w-]+)/', FamilyDetailView.as_view(), name='details'),
    url(r'^list/', FamilyListView.as_view(), name='list'),
    url(r'^familymap/', familyMap, name='familyMap'),
    url(r'^camps/', viewRefugeeCamp, name='camps'),
    url(r'^donate/', donate, name='donate'),
    url(r'^adddonate/', adddonate, name='adddonate'),
]
