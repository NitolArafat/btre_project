from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
from contacts.models import Contacts


def contact(request):
     if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']


        contacts = Contacts(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,
                         message=message,user_id=user_id)

        if request.user.is_authenticated:
            user_id=request.user.id
            has_connected=Contacts.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_connected:

                messages.error(request,'You are already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)


            contacts.save()





        send_mail(
            'Property Listing Inquiry',
            'There has been inquiry for ' + listing + ', please contact with our for more info',
            'mdaaanitol@gmail.com',
            [realtor_email,'mda3anitol@gmail.com'],
            fail_silently=False,
        )



        messages.success(request,'Your request has been submitted, a realtor will get back to you soon ')

        return redirect('/listings/'+listing_id)

