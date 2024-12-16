from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    phone = models.CharField(max_length=15) 
    whatsapp = models.CharField(max_length=15, blank=True, null=True)  
    facebook = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return self.name