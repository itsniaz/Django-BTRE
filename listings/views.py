from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Listing



def listings(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 3)

    page = request.GET.get('page')

    listing_slot = paginator.get_page(page)

    context = {
        'listings' : listing_slot
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