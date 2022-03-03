from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import authenticate, get_user_model
from django.utils.text import capfirst

from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name= forms.CharField(error_messages={'required': 'Please enter your first name'})
    last_name= forms.CharField(error_messages={'required': 'Please enter your last name'})
    username= forms.CharField(error_messages={'required': 'Please enter your usernamename'})
    email= forms.EmailField(help_text='Format: 123@gmail.com, 456@yahoo.com',error_messages={'required': 'Please enter your email address'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields=['first_name','last_name','username','email','password1','password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
class RequestForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Request
        fields=['name','email','phone_number','image','price']
    