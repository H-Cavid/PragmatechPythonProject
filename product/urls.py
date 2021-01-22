from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>/', ProductDetail.as_view(), name='product_detail')
]

