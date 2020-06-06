from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Listings
from listings.choices import bedroom_choices,price_choices,aria_choices





def index(request):

    #listings=Listings.objects.all()
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings, 6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)




    context={
        'listings': paged_listings,
    }
    return render(request,'listings/listings.html',context)
   # return HttpResponse('<h1>nitol arafat</h1>')



def listing(request,listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    context={
        'listing': listing
    }
    return render(request,'listings/listing.html',context)


def search(request):

    queryset_list=Listings.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
        #print(request.GET)
        keywords= request.GET['keywords']
        if keywords:
            queryset_list=Listings.objects.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=Listings.objects.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=Listings.objects.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = Listings.objects.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = Listings.objects.filter(price__lte=price)


    context={
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': aria_choices,
        'listings':queryset_list,
        'values':request.GET
    }
    return render(request, 'listings/search.html',context)
