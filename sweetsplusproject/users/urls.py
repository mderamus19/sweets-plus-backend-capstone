"""Define URL patterns for users"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    #Default auth urls
    path('', include('django.contrib.auth.urls')),
]
