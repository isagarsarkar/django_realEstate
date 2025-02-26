from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name =  models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.TextField()
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name    
