from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('test', views.listing, name='listing'),

]
