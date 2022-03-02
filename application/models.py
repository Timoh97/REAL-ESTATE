


# Create your models here.
import email
from django.db import models

#ordersystem
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
import cloudinary
from cloudinary.models import CloudinaryField




class User(AbstractUser):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255, unique=True)
    email=models.EmailField(unique=True)
    password1=models.CharField(max_length=255)
    password2=models.CharField(max_length=255)
    def __str__(self):
     return self.username
    


    
    
