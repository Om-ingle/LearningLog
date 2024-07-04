"""Defines URL patterns for users"""

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    # Other URLS,
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]