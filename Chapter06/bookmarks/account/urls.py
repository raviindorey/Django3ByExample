from django.urls import path, include

from .views import dashboard, register, edit, user_list, user_detail

urlpatterns = [
    path('edit/', edit, name='edit'),
    path('register/', register, name='register'),
    path('users/', user_list, name='user_list'),
    path('users/<username>', user_detail, name='user_detail'),
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
]
