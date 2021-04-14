from django.shortcuts import render, redirect
from category.models import *
from staticpage.models import *
from product.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.mixin import DRF
from django.views.generic import TemplateView,View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
# Create your views here.

class ProductViews(APIView):
    def get(self,request):
        product=Product.objects.all()#butun productlarimizi getirirk
        serializer=ProductSerializers(product,many=True)#serializer-in icine prodcutlarimizi gonderirikki bir bir cevirsin
        return Response(serializer.data)#response kimide serializerin datasini gonderirik

    def post(self,request):
        serializer=ProductSerializers(data=request.data)##menim serializerim=di productdserializerden gelen dataya
        if serializer.is_valid():
            serializer.save()#eger serializer-da data varsa save elyirik
            return Response(serializer.data,status=status.HTTP_201_CREATED)#created cavabini gonderirik
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)#yoxdussa 400 error qaytaririq

class ProductDetailViews(APIView):
    def get(self,request,id):
        product=Product.objects.get(id=id)
        serializer = ProductDetailSerializers(product)
        return Response(serializer.data)

    def put(self,request,id):
        serializer=ProductDetailSerializers(data=request.data)##menim serializerim=di productdserializerden gelen dataya
        if serializer.is_valid():
            serializer.save()#eger serializer-da data varsa save elyirik
            return Response(serializer.data,status=status.HTTP_201_CREATED)#created cavabini gonderirik
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)#yoxdussa 400 error qaytaririq

    def delete(self,request,id):
        product=Product.objects.get(id=id)
        del product
        return Response({"success":"Mehsul silindi"})






















def index(request):
    # categories = Category.objects.prefetch_related('sub_categories').all()
    # c = Category.objects.get(id=1)
    # a = c.r()
    # print(a)
    
    sliders = Slider.objects.all()
    #request.session['test'] = 10
    print(request.session.items())
    products = Product.objects.all()[:10]
    context = {
        # 'categories':categories,
        'sliders':sliders,
        # 'c': c,
        'products':products, 
    }
    return render(request,'index.html', context)
    
@csrf_exempt
def add_to_wishlist(request,id):
    if request.method == "POST":
        if not request.session.get('wishlist'):
            request.session['wishlist'] = list()
        else:
            request.session['wishlist'] = list(request.session['wishlist'])
        items = next((item for item in request.session['wishlist'] if item['id']==id),False)
    add_data = {
        'id':id,
    }
    if not items:
        request.session['wishlist'].append(add_data)
        request.session.modifier = True
    return redirect('index')

@csrf_exempt
def remove_wishlist(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        for i in request.session['wishlist']:
            if str(i['id']) == id:
                i.clear()
        while {} in request.session['wishlist']:
            request.session['wishlist'].remove({})
        if not request.session['wishlist']:
            del request.session['wishlist']
    try:
        request.session['wishlist'] = list(request.session['wishlist'])
    except:
        pass
    request.session.modifier = True
    return JsonResponse({'status':'ok'})


