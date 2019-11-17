from django.shortcuts import render
from django.http import HttpResponse

from btre.choices import state_choices,price_choices,bedroom_choices
from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    context = {
      'listings':listings,  
      'state_choices':state_choices,
      'price_choices' :price_choices,
      'bedroom_choices':bedroom_choices
    }
    return render(request,"pages/index.html",context)

def about(request):
    return render(request,"pages/about.html")    

