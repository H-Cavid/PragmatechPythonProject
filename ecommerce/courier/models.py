from django.db import models
from backend.models import User
from order.models import Order
import uuid
from utils.genslug import gen_slug
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from decimal import Decimal
# Create your models here.

class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    courier_price = models.DecimalField(max_digits=100,decimal_places=2,default=2.00)
    order_end_total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)

    def __str__(self) -> str:
        return str(self.id)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug= gen_slug(self.user.username)
        super().save(*args,**kwargs)

# orderin qiymetini tap ustune price-i gel totalda goster
@receiver(pre_save,sender=Courier)
def courier_signal(sender,*args,**kwargs):
    order_price=Order.objects.all()
    # print(order_price) <OrderQuerySet [<Order: Order object (1)>]>
    order_end_total1 = 0 #default onsuz 0-di her ehtimala
    for x in order_price:#queryseti obyekte cevirmek ucun yoxsa cixanmiram  totalina
        # print(x) Order object (1)
        #  print(x.cart.total) 91486.80
        if order_end_total1<x.cart.total:
            order_end_total1=x.cart.total+courier_price
            order_end_total=order_end_total1
            order_end_total.save()
            


    