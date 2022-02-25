from django.urls import path
from . import views



urlpatterns = [
path('', views.index, name='index'),
path("login/", views.login, name="login"),
path("signup/", views.signup, name="signup"),
path("about/", views.about, name="about"),
path("agent/", views.agent, name="agent"),
path("client/", views.client, name="client"),

#authentication
path('signup/', views.signup,name='signUp'),
path('signup/donors/', views.donor_signup,name='customer_signup'),
path('signup/NGO/', views.ngo_signup,name='author_signup'),
path('login/',views.login_view, name = 'login_view'),   
path('logout/', views.logout, name='logout'),
]