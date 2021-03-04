from django.urls import path
from .views import *

urlpatterns = [
    #path('<cat_slug>/<subcat_slug>/<brand_slug>', subcategory_brands, name='subcategory_brands'),
    path("category/subcategory/brands/<slug>/" , brands_product, name="brands_product"),
    
    # path('<cat_slug>/<subcat_slug>/<brand_slug>/<product_slug>', brand_products, name='brand_products'),
]
