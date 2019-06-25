from django.contrib import admin

# Register your models here.
from .models import Camps, CampsFacl, CampsItems

admin.site.register(Camps)
admin.site.register(CampsFacl)
admin.site.register(CampsItems)
