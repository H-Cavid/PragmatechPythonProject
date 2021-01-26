from django.shortcuts import render
from product.models import *
from django.views.generic import DetailView
from analytics.mixins import ObjectViewedMixin
from cart.models import Cart


# class ProductDetail(ObjectViewedMixin,DetailView):
#     queryset = Product.objects.all()
#     template_name = 'product/product.html'

#     def get_context_data(self, **kwargs):
#         context = super(ProductDetail,self).get_context_data(**kwargs)
#         context["cart"] = 'okey'
#         return context
    
#     def get_object(self,*args, **kwargs):
#         request = self.request
#         id = self.kwargs.get('id')
#         user = request.user
#         instance = Product.objects.get(id=id)
#         return instance

def product(request):
   
    product = Product.objects.get(id=1).get_downloads
    
    print(product)
    
    context = {
        'product':product,
        'user': request.user

    }
    return render(request, 'product/product.html',context)


from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "product/product.html"