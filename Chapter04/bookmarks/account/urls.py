from django.urls import path, include

from .views import dashboard, register

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
