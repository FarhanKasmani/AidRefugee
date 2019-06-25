from django.contrib import admin

# Register your models here.

from .models import Family

class FamilyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'family_members']
    class Meta:
        model = Family

admin.site.register(Family, FamilyAdmin)
