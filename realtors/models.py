from django.db import models
from datetime import datetime
class Realtor(models.Model):
    title = models.CharField(max_length=200)
    name  = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d")
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    isMVP = models.BooleanField(default=False)
    hireDate = models.DateField(default=datetime.now)

    def __self__(self):
        return self.name