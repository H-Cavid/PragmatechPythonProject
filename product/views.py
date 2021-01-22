from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
from analytics.mixins import ObjectViewedMixin
from cart.models import Cart

class ProductDetail(ObjectViewedMixin,DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail,self).get_context_data(**kwargs)
        #cart_obj = Cart.objects.new_or_get(self.request)
        context["cart"] = 'okey'
        return context
    
    def get_object(self,*args, **kwargs):
        request = self.request
        id = self.kwargs.get('id')
        instance = Product.objects.get(id=id)
        return instance

def product(request,id):
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    
   
    
    context = {
        'pro':products,
        'user': request.user

    }
    return render(request, 'product/product.html',context)


