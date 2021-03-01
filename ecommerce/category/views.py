from django.shortcuts import render
from category.models import Category
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse
# Create your views here.

def category(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'category.html', context)

@csrf_exempt
def category_products(request, slug):
    products = Category.products_in_category(slug)
################POST###############    
    if request.method == "POST":
        data2 = request.POST.get ("q")#requestden datani goturruk
        url = "https://api.teammers.com/project/packets/%7B%7D/?format.json".format(data2)#burda url-e elave elyirik hemin data-ni
        a = requests.get(url)#burdada hemin url-e request gonderirik
        print(a.text)
################GET###############
    try:
        data = request.GET.get("q")
        url = "{}".format(data)
        a = requests.get(url)
        return HttpResponse(a.text)
    except:
        pass

    context = {
        'products':products
    }
    return render(request, 'category_products.html', context)