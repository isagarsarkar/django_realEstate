from django.shortcuts import render
from django.http import Http404
from .models import Listing
from django.core.paginator import Paginator
from btre.choices import state_choices,price_choices,bedroom_choices


def index(request):
    listings =  Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 1) # Show 1 contacts per page

    page = request.GET.get('page')
    pages_listings = paginator.get_page(page)
    context = {
       'listings': pages_listings,
    }
    return render(request,'listings/index.html',context)

def listing(request,listing_id):
        try:
            listing = Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            raise Http404('Record does not exist')
        #print(listing.query)
        context = {
            'listing': listing
        }
        return render(request,'listings/listing.html',context)

def search(request):
     listings =  Listing.objects.order_by('-list_date').filter(is_published=True)
     if 'keywords' in request.GET:
         keywords = request.GET['keywords']
         if keywords:
             listings = listings.filter(description__icontains=keywords)
     if 'city' in request.GET:
         city = request.GET['city']
         if city:
             listings = listings.filter(city__iexact=city)
     if 'state' in request.GET:
         state = request.GET['state']
         if state:
             listings = listings.filter(state__iexact=state) 
     if 'bedrooms' in request.GET:
         bedrooms = request.GET['bedrooms']
         if bedrooms:
             listings = listings.filter(bedrooms__lte=bedrooms)
     if 'price' in request.GET:
         price = request.GET['price']
         if price:
             listings = listings.filter(price__lte=price)                                   
     context = {
       'listings': listings,
       'state_choices':state_choices,
       'price_choices' :price_choices,
       'bedroom_choices':bedroom_choices,
       'values':request.GET
      }
     return render(request,'listings/search.html',context)
