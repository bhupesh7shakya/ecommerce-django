from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('user/registration',views.UserRegistrationView.as_view(),name="user-registration"),
  path('user/login',views.UserLoginView.as_view(),name="user-login"),
]