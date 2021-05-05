from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.core.mail import send_mail
from django.core.management import settings
from django.shortcuts import render,redirect
from django.http import JsonResponse


class ResetPasswordEmail(APIView):
    serializer_class = EmailSerializers

    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        email = serializers.validated_data['email']
        check_user = User.objects.filter(email=email)
        if check_user.count() > 0:
            get_user = User.objects.get(email=email)
            create_very = UserVerify.objects.get_or_create(user_id=get_user.id)
            subject = "Shifrenin berpasi ucun"
            message = "Ashagdaki linke daxil olun \n\n http://127.0.0.1:8000/check_email?token={}".format(create_very[0].token)
            recepient = "{}".format(get_user.email)
            send_mail(subject,message,settings.EMAIL_HOST_USER, [recepient],fail_silently=True)
            return Response({'success':'Email gonderildi'})
        return Response({'data':'None'})


def check_email(request):
    if request.method == "GET":
        token = request.GET.get('token')
        try:
            check_token = UserVerify.objects.get(token=token)
            return redirect('http://127.0.0.1:8000/password_resed/?token=' + f"{check_token.token}")
            # check_token.delete()
        except:
            return JsonResponse({'error':"Invalid Token"})
    return JsonResponse({"data":"None"})
        
        
class PasswordResetViwe(APIView):
    serializer_class = PasswordResetSerializers
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        token = request.GET.get('token')
        try:
            check_token = UserVerify.objects.get(token=token)
            get_user = User.objects.get(id=check_token.user.id)
            get_user.set_password(serializers.validated_data['password'])
            get_user.save()
            check_token.delete() 
            return Response({"success":"Sifre ugurla deyisdirildi"})
        except:
            return Response({"fail":"Token is not valid"})



        