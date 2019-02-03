from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ["title","realtor","price","list_date","is_published"]
    list_display_links = ["title"]
    list_editable = ["realtor","price","list_date","is_published"]
    list_filter = ["price","list_date"]
    search_fields = ["title","address"]
   
    

admin.site.register(Listing, ListingAdmin)