from django.shortcuts import render
from category.models import *

# Create your views here.

def brands_product(request,slug):
    brands = Brand.products_in_brand(slug)
    context = {
        "brand" : brands
    }

    return render(request, "brand.detail.html" , context)