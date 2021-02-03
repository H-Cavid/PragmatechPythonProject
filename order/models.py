from django.db import models

# Create your models here.
from cart.models import Cart


class Order(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,blank=True,null=True)
    user_order=models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    order_id=models.CharField(max_length=100,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto-now=False)
    

    
