from django.urls import path
from .views import *


urlpatterns = [
    path('add_to_card/<int:id>/',add_to_card,name='add_to_card'),
    path('cards/',cards_products,name='cards_products'),
]