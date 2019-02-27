from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone","photo"]
    list_display_links = ["email"]
    list_editable = ["name"]
    search_fields = ["name","email","phone","photo"]
    

admin.site.register(Realtor, RealtorAdmin)