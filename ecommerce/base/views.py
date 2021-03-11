from django.shortcuts import render
from category.models import Category
from staticpage.models import Slider

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    slider = Slider.objects.all()
    context = {
        'categories':categories,
        "sliders" : slider
    }
    return render(request,'index.html',context)

