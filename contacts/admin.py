from django.contrib import admin
from .models import Contact
from listings.models import Listing

def get_realtor_name(obj):
   listing =  Listing.objects.get(id=obj.listing_id)
   return listing.realtor.name

get_realtor_name.short_description = "Realtor"   

class ContactAdmin(admin.ModelAdmin):
     list_display = ('id','name','listing','email','phone',get_realtor_name)
     list_display_links = ('id','name')
     list_per_page = 10
     list_filter = ('name','email')
     search_fields = ('name','email')

admin.site.register(Contact,ContactAdmin)     


