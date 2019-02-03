from django.shortcuts import render
from .models import Listing




def listings(request):
    listingsList = Listing.objects.all()


    context = {
        'listings' : listingsList
    }

    return render(request, "pages/listings.html", context)

def listing(request):
    return render(request,"pages/listing.html")

def search(request):
    return render(request, "pages/search.html")