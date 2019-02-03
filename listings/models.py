from django.db import models
from realtors.models import Realtor
from datetime import datetime

class Listing(models.Model):
    realtor   = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title     = models.CharField(max_length=200)
    address   = models.CharField(max_length=250)
    price     = models.IntegerField()
    description = models.TextField(max_length=600)
    city      = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    zipcode   = models.CharField(max_length=200)
    bedrooms  = models.IntegerField()
    bathrooms = models.IntegerField()
    garage    = models.IntegerField(default=0)
    sqft      = models.DecimalField(max_digits=5, decimal_places=1)
    lot_size  = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=False)
    photo_main =  models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1    = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_2    = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_3    = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_4    = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_5    = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_6    = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    list_date  = models.DateTimeField(default=datetime.now())    

    def __str__(self):
        return self.title
