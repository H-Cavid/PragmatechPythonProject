from django.urls import path
from .views import *


urlpatterns = [
    path('register', get_register , name='get_register'),
    path('login', get_login , name='get_login'),
    path('logout', get_logout, name = 'get_logout')
]