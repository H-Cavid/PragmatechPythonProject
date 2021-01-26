from django.urls import path
from .views import *


urlpatterns = [
    path('', product, name='product_detail'),
    path('about/', AboutView.as_view()),
]

