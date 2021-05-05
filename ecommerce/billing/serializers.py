from rest_framework import serializers
from billing.models import BillingProfile,Card


class BillingProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = BillingProfile
        fields = "__all__"

class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"