from django.db import models
from django.db.models.fields import CharField
from backend.models import User
from order.models import Order
import uuid
from utils.genslug import gen_slug
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from decimal import Decimal
# Create your models here.

STATUS = (
    ('ÇATDIRILDI','ÇATDIRILDI'),
    ('YOLDADIR','YOLDADIR'),
)
##############
"LogData model yaranmalidi"
"LogData model courier-e bagli olmalidi"
"Eger courier-in statusu catdirildi olarsa logdata modeli create olunmalidi ve curyerin melumatlari logdatada text formatinda qeyd olunmalidi"

##############
class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    courier_price = models.DecimalField(max_digits=100,decimal_places=2,default=2.00)
    order_end_total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    status = models.CharField(max_length=100,choices=STATUS,blank=True,null=True)

    def __str__(self) -> str:
        return str(self.id)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug= gen_slug(self.user.username)
        if not self.order:
            self.order_end_total = 0
        else:
            self.order_end_total = Decimal(self.order.cart.total) + Decimal(self.courier_price)
        super().save(*args,**kwargs)
        
    def parse_data_log(self):
        return "ID-si {}  olan kuryer ,{} nömrəli sifarişi ,{} qiymətə , {} adresə çatdırdı!".format(self.id,self.order.id,self.order_end_total,self.order.shipping_address_final)

class LogData(models.Model):
    courier = models.ForeignKey(Courier,on_delete=models.CASCADE,blank=True,null=True)
    log = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self) -> str:
        return str(self.id)

@receiver(pre_save,sender=Courier)
def show_log(instance,*args,**kwargs):
    if instance.status == 'ÇATDIRILDI':
        log_data = instance.parse_data_log()
        LogData.objects.create(courier_id=instance.id,log = log_data)



# # orderin qiymetini tap ustune price-i gel totalda goster
# @receiver(post_save,sender=Courier)
# def courier_signal(sender,instance,*args,**kwargs):
#     order_price=Order.objects.all()
#     # print(order_price) <OrderQuerySet [<Order: Order object (1)>]>
#     order_end_total1 = 0 #default onsuz 0-di her ehtimala
#     for x in order_price:#queryseti obyekte cevirmek ucun yoxsa cixanmiram  totalina
#         # print(x) Order object (1)
#         #  print(x.cart.total) 91486.80
#         if order_end_total1<x.cart.total:
#             order_end_total1=Decimal(x.cart.total)+Decimal(instance.courier_price)
#             print(instance.courier_price)#4
#             print(instance.order_end_total)#2333.00
#             instance.order_end_total=order_end_total1
#             print(instance.order_end_total)#91490.80
#             print(order_end_total1)#91490.80
#             instance.order_end_total.save()
            
# # 4.00
# # 2333.00
# # 91490.80
# # 91490.80
##instance yaranan obyekti sender classdi instance obyekt kimi sender ise cclass kimi qaytarir
#post_save created argument verir qisada pre_save meqsede uygundu