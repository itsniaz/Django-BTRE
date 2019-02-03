from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone","photo"]
    

admin.site.register(Realtor, RealtorAdmin)