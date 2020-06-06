from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices,aria_choices

# Create your views here.
def index(request):
    listings=Listings.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': aria_choices,

    }
    #return HttpResponse('<h1>nitol arafat</h1>')
    return render(request,'pages/index.html',context)


def about(request):
    # Get all realtors
    realtors=Realtor.objects.order_by('-hire_date')
    # Get mvp
    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)

    context={
      'realtors': realtors,
      'mvp_realtors': mvp_realtors

    }
    return render(request,'pages/about.html',context)