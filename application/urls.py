from django.urls import path

from . import views



urlpatterns = [
path('', views.index, name='index'),
path("login/", views.loginView, name="login"),
path("signup/", views.signup, name="signup"),
path("about/", views.about, name="about"),
path("agents/", views.agent, name="agent"),
path("clients/", views.client, name="client"),
path("reviews/", views.reviews, name="reviews"),
path("gallery/", views.gallery, name="gallery"),
path("request/", views.request, name="request"),

#authentication

]