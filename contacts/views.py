from django.shortcuts import render, redirect
from listings.models import Listing
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = Listing.objects.get(id=listing_id)
        if listing is not None:
            listing_title = listing.title
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            if request.user.id is not None:
               user_id = request.user.id
               is_contacted =  Contact.objects.filter(user_id=user_id,listing_id=listing_id)
               if is_contacted:
                   messages.error(request,"You already contacted for this property")
                   return redirect("/listings/"+listing_id)

            else:
               user_id = 0    
            contact = Contact(listing=listing_title,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
            contact.save()
            #send email
            send_mail(
                'Property Enquiry',
                'Thanks for showing interest in '+listing_title,
                'smtpsagar19@gmail.com',
                [email],
                fail_silently=False,
            )
            messages.success(request,"Thanks for showing interest. Our realtor will get back to you soon")
        else:
            messages.error(request,"There is some issue. Please check and try later")
        return redirect("/listings/"+listing_id)    
   
