from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request):

    listings = Listing.objects.all()
 
    context = {
        'listings' : listings
    }

    return render(request, "pages/index.html", context)


def about(request):

    realtors = Realtor.objects.all()

    context = {

        "realtors" : realtors
    }

    return render(request, "pages/about.html", context)


def listings(request):
    return render(request, "pages/listings.html")
