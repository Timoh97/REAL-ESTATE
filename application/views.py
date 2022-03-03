from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

#importations for resetting password via email
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

#solving custom user and inbuilt django user
from django.contrib.auth import get_user_model
User = get_user_model()




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
    
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/request')
        else:
            form=SignUpForm()
     return render(request, 'request.html')

#REGISTRATION WITH A WELCOME EMAIL
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            subject = 'Welcome to the EQUINOX!'
            message = f'Hi {user.first_name},\nThe EQUINOX real estate would like to officially welcome you to our growing community.See what you would like to purchase, and contact us.\nRemember to enjoy the app!\n\nKind Regards,\nThe EQUINOX Management.'
            email_from = settings.EMAIL_HOST_USER
            email=email
            recepient_list = [user.email]
            send_mail(subject,message,email_from,recepient_list)
            messages.success(request, 'Account created successfully! Check your email for a welcome mail')
            return redirect('login/')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})


    
    return render(request,'registration/signup.html',{'form':form})


def loginView(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = LoginForm()
	return render(request=request, template_name="registration/login.html",context= {"form":form})




#resetting password vial email
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_email/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})