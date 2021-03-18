from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_to_wishlist/<int:id>/',add_to_wishlist,name='add_to_wishlist'),
    path('remove_wishlist/', remove_wishlist,name='remove_wishlist'),
    path('add_to_producthistory/<int:id>/',add_to_producthistory,name='add_to_producthistory'),
]