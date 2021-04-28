from django.shortcuts import render
from rest_framework.views import APIView
from billing.models import BillingProfile,Card
from rest_framework.response import Response
from billing.serializers import BillingProfileSerializers

# Create your views here.

class BillingProfileViews(APIView):
    def get(self,request,format=None):
        profiles=BillingProfile.objects.all()
        serializer =  BillingProfileSerializers(profiles,many=True)
        return Response(serializer.data)

class CardViews(APIView):
    def get(self,request,format=None):
        cards=Card.objects.all()
        serializer = CardSerializers(cards,many=True)
        return Response(serializer.data)