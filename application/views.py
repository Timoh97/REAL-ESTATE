from django.shortcuts import render



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
     '''View function to present users with account choices'''
     title = 'Sign Up'
     return render(request,'registration/signup.html',{'title': title})

def login(request):
     '''View function to present users with account choices'''
     title = 'Login'
     return render(request,'registration/login.html',{'title': title})