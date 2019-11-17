from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','realtor')
    list_display_links = ('id','title')
    list_per_page = 10
    list_editable = ('is_published',)
    list_filter = ('realtor',)
    search_fields = ('title','address','zipcode','city','state')

admin.site.register(Listing,ListingAdmin)
