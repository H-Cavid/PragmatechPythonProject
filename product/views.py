from django.shortcuts import render
from .models import *


def product(request,id):
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    
   
    
    context = {
        'pro':products,
        'user': request.user

    }
    return render(request, 'product/product.html',context)


