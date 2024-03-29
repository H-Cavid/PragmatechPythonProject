from .models import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from backend.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from backend.serializers import UserProfileSerializers

class LoginTokenView(TokenObtainPairView):
    serializer_class = TokenPairSerializers


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers


class UserDetail(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        user = User.objects.filter(id=self.request.user.id)
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)

class UserProfile(APIView):
    def get(self,request):
        user_profile=Profile.objects.all()
        serializer = UserProfileSerializers(user_profile,many = True)
        return Response(serializer.data) 
    

    def post(self, request, format=None):
        serializer = UserProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)