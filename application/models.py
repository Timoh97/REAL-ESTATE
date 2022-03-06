


# Create your models here.
import email
from email.policy import default
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
    email=models.EmailField(unique=False)
    phone_number=models.IntegerField(blank=False)
    plot_no=models.IntegerField(unique=True)
    trans_id=models.CharField(max_length=255, default='')
    number_of_rooms=models.IntegerField(blank=True, null=True)
    security=models.CharField(max_length=255, default='')
    power_vailability=models.BooleanField(default=False)
    water_availability=models.BooleanField(default=False)
    furnished=models.CharField(default='',max_length=400)
    # image=CloudinaryField('image')
    image = models.ImageField(upload_to='images/')
    description=models.CharField(max_length=400,default='')
    price=models.IntegerField(blank=False)
    datetime = models.DateTimeField(auto_now=True)
    admin_approved = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    
    def __str__(self):
     return self.name


    
    
