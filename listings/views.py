from django.shortcuts import render

def listings(request):
    return render(request, "pages/listings.html")

def listing(request):
    return render(request,"pages/listing.html")

def search(request):
    return render(request, "pages/search.html")