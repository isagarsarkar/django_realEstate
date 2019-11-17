from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','hire_date','is_mvp')
    list_display_links = ('id','name')
    list_per_page = 10
    list_editable = ('is_mvp',)
    list_filter = ('hire_date',)
    search_fields = ('name','email','phone')

admin.site.register(Realtor,RealtorAdmin)
