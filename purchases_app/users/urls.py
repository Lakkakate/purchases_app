from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from .views import login_user, logout_user

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
