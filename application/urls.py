from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


# app_name = "application" 

urlpatterns = [
path('', views.index, name='index'),
path("login/", views.loginView, name="login"),
path("signup/", views.signup, name="signup"),
path("about/", views.about, name="about"),
path("agents/", views.agent, name="agent"),
path("clients/", views.client, name="client"),
path("reviews/", views.reviews, name="reviews"),
path("gallery/", views.gallery, name="gallery"),
path("details/", views.details, name="details"),
path("request/", views.request, name="request"),
# path("search/", views.search_product, name="search")
path("password_reset/", views.password_reset_request, name="password_reset"),
# path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),      

#authentication
#password restting


]