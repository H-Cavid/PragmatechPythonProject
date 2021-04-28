from rest_framework import serializers
from product.models import Product,ProductFile
from brand.models import Brand
from category.models import Category,SubCategory
#id-si varsa informasiyasi gorunmerse id yazilmalidi
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = "__all__"
class SubCategorySerializers(serializers.ModelSerializer):
    category=CategorySerializers(read_only=True)
    class Meta:
        model = SubCategory
        fields = "__all__"
class BrandSerializers(serializers.ModelSerializer):
    sub_category=SubCategorySerializers(read_only=True)
    class Meta:
        model = Brand
        exclude = ["brand_slug"]

class ProductFileSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductFile
        exclude = ["product"]

class ProductSerializers(serializers.ModelSerializer):
    brand=serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()#database-da bele bir sey yoxdu api-da gorunur ancaq bu
    sub_category=serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_category(self,obj):#burda get_yazdigimiz fieldin adi,default olaraq obj qebul elyir
        # s=float(obj.product_price)
        # o=str(s)
        # return  o
        ids = obj.product_brand.sub_category.category.id
        category = obj.product_brand.sub_category.category.name
        data = {
            "id":ids,
            "category_name":category,

        }
        return data
    

    def get_sub_category(self,obj):
        product_sub_category=obj.product_brand.sub_category.name
        data = {
            "sub_category_name":product_sub_category,
        }
        return data
    
    def get_brand(self,obj):
        product_brand=obj.product_brand.name
        data = {
            "product_brand_name":product_brand,
        }
        return data

class ProductDetailSerializers(serializers.ModelSerializer):
    product_brand = BrandSerializers(read_only=True)
    productfile_set=ProductFileSerializers(many=True)
    # brand=serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    # def get_brand(self,obj):
    #     ids = obj.product_brand.id
    #     brand=obj.product_brand.name
    #     data = {
    #         "id":ids,
    #         "brand_name":brand,
    #     }
    #     return data