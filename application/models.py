


# Create your models here.
import email
from enum import unique
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
class Request(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone_number=models.IntegerField()
    image=CloudinaryField('image')
    description=models.CharField(max_length=400,default='')
    price=models.IntegerField()
    def __str__(self):
     return self.name


    
    
