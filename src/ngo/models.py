from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()
class Camps(models.Model):
    user            = models.ForeignKey(User, related_name='ngo_user', null=True, blank=True)
    name            = models.CharField(max_length=20)
    latitude = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)

    def __str__(self):
        return self.user.email
    def __unicode__(self):
        return self.user.email

class CampsItems(models.Model):
    camp = models.ForeignKey(Camps, null=True, blank=True)
    items = models.CharField(max_length=20)

class CampsFacl(models.Model):
    camp = models.ForeignKey(Camps, null=True, blank=True)
    facl = models.CharField(max_length=20)
