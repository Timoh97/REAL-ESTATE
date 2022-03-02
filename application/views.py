from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.views.generic import CreateView
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    
    
    return render(request, 'index.html')
def about(request):
    
    
    return render(request, 'about.html')

def agent(request):
        
    
    return render(request, 'agent.html')
def client(request):
    
    
    return render(request, 'client.html')

   


def reviews(request):
    
    
    return render(request, 'reviews.html')

def gallery(request):
    
    
    return render(request, 'gallery.html')
def request(request):
    
    
    return render(request, 'request.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


    
    return render(request,'registration/signup.html',{'form':form})

def loginView(request):
  form = LoginForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
       login(request,user)
         
      return redirect('/')
      
  
  return render (request, 'registration/login.html',{'form':form})
 
 
 #mpesa api
