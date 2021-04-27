from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('user-account/', views.user_account,name='user_account'),
    path('login/', views.login,name='login'),

   
]