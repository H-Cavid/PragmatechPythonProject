from rest_framework import serializers
from billing.models import BillingProfile
from order.models import Order
from backend.models import User



class OrderSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude =["billing_profile","shipping_address","billing_address",]

class BillingProfileSerializers(serializers.ModelSerializer):
    billing_profile=OrderSerialziers(many=True,read_only=True)
    class Meta :
        model = BillingProfile
        exclude = ["user",]

class UserSerializers(serializers.ModelSerializer):
    billing_user=BillingProfileSerializers()
    class Meta:
        model = User
        fields = ["billing_user",]

    