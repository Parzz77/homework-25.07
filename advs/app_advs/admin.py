from django.contrib import admin
from .models import Advertisment

class AdvertismentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Advertisment, AdvertismentAdmin)

# Register your models here.
