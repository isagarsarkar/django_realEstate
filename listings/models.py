from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address =  models.CharField(max_length=200)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=20,blank=True)
    description = models.TextField(blank=True)
    price =models.IntegerField(default=100)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1,default=1)
    garage = models.IntegerField(default=0)
    sqft =models.IntegerField(default=100)
    lot_size = models.DecimalField(max_digits=5,decimal_places=1,default=1)
    is_published = models.BooleanField(default=True)
    list_date =  models.DateTimeField(default=datetime.now,blank=True)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d",blank=True)

    def __str__(self):
        return self.title