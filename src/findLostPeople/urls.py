from django.conf import settings
from django.conf.urls import url
from .views import findPeople

urlpatterns = [
    url(r'^find/', findPeople, name='find'),
]
