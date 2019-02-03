from django.shortcuts import render,get_object_or_404
from .models import Listing




def listings(request):
    listingsList = Listing.objects.all()



    context = {
        'listings' : listingsList
    }

    return render(request, "pages/listings.html", context)

def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing' : listing
    }

    return render(request,"pages/listing.html", context)

def search(request):
    return render(request, "pages/search.html")