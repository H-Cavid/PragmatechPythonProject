from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from backend.models import User

# Create your views here.
class UserDetail(APIView):

    def get(self,request):
        user=User.objects.filter(id=self.request.user.id)
        serializer=UserSerializers(user,many=True)
        return Response(serializer.data)

