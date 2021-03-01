from django.db import models
from address.models import Address
from billing.models import BillingProfile
from backend.models import User
from cart.models import Cart
from datetime import datetime, timedelta
from django.utils import timezone


# Create your models here.

ORDER_STATUS_CHOICES=(
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)
#her bir statusa gore filtr lazimdi
#vaxt araligina gore filterler default 7 gunluk ve 2 heftelik
#son 9 gunun filteri
#indiki vaxtdan 9 gun cixiriq update-e gore gtye-ye gore <=dire gore filterler
#today = datetime.now().date()


     


















class OrderQuerySet(models.QuerySet):

    def by_status(self,status='created'):
        return self.filter(status=status)


    def by_range(self, start_date, end_date=None):
        if end_date is None:
            return self.filter(update__gte=start_date)
        return self.filter(update__gte=start_date).filter(update__lte=end_date)


    def by_weeks_range(self,weeks_ago=2,number_of_weeks=3):
        if number_of_weeks > weeks_ago:
            number_of_weeks = weeks_ago
        day_ago_start = weeks_ago * 7
        print(day_ago_start)
        day_ago_end = day_ago_start - (number_of_weeks * 7)
        print(day_ago_end)
        start_date = timezone.now() - timedelta(days=day_ago_start)
        print(timedelta(days=day_ago_start))
        end_date = timezone.now() - timedelta(days=day_ago_end)
        print(end_date)
        print(start_date)
        return self.by_range(start_date,end_date=end_date)













#     def created_orders(self):
#         return self.object.filter(status = "created")
    
#     def paided_orders(self):
#         return self.object.filter(status = "paid")

#     def shipped_orders(self):
#         return self.object.filter(status = "shipped")

#     def refunded_orders(self):
#         return self.object.filter(status = "refunded")
    
#     def filter_by_week(self):
#         today = datetime.today()
#         week_result= today - timedelta(days=7)
#         orders=Order.object.filter(timestamp__gte=week_result)#self yoxsa instance deqiq bilmirem field-e nece cixim
#         return orders

#     def filter_by_twoweek(self):
#         today = datetime.today()
#         twoweek_result= today - timedelta(days=14)
#         orders=Order.object.filter(timestamp__gte= twoweek_result)
#         return orders

#     def filter_by_ninedays(self):
#         today = datetime.today()
#         ninedays_result = today - timedelta(days=9)
#         orders=Order.object.filter(timestamp__gte=ninedays_result)  
#         return orders
    
 
class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQueryset(self.model , using=self._db)
    # def filter_by_week(self):
    #     return self.get_queryset().filter_by_week()#teze  versiyada qeydiyyatdan kecirmeliyem
    def by_weeks_range(self):
        return self.get_queryset().by_weeks_range()
    def by_status(self,status='created'):
        return self.get_queryset().by_status(status=status)

class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE,related_name='billing_profile',blank=True,null=True)
    order_id = models.CharField(max_length=100,blank=True)
    shipping_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='shipping_address',blank=True,null=True)
    billing_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='billing_address',blank=True,null=True)
    shipping_address_final = models.TextField(blank=True,null=True)
    billing_address_final = models.TextField(blank=True,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,default='created',choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=1.00,max_digits=60,decimal_places=2)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    object = OrderManager()






