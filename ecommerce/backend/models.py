from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from datetime import datetime,timedelta
from django.core.management import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
# Create your models here.

class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    is_branch = models.BooleanField(default=True)
    is_delivery = models.BooleanField(default=True)
    is_phone_status = models.BooleanField(default=False)


class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address_name = models.CharField(max_length=40)
    home = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class UserOtp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_otp')
    otp = models.CharField(max_length=6)
    rpt = models.IntegerField(default=3)
    date = models.DateTimeField(auto_now=True)

class UserVerify(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=400,blank=True,null=True)
    status = models.BooleanField(blank=True,null=True)
    date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.token

    def save(self,*args, **kwargs):
        self.token = ""
        if not self.token:
            self.token = self._create_verify_token()
        if not self.date:
            self.date = datetime.now()+ timedelta(minutes=1)
        super().save(*args,**kwargs)

    def _create_verify_token(self):#protected method(enkapsulyasiya)
        dt = datetime.now() + timedelta(days = 13)
        token = jwt.encode({
            "id" : self.id,
            'exp' : int(dt.timestamp())
        },settings.SECRET_KEY,algorithm = 'HS256')
        return token

@receiver(post_save,sender=User)
def email_very(sender,instance,created,**kwargs):
    if created is True:
        create_verify_email = UserVerify.objects.get_or_create(user_id=instance.id)
        subject = "Emaili tesdiqlemek ucun asagidaki linke daxil olun!"
        message = "Ashagdaki linke daxil olun \n\n http://127.0.0.1:8000/check_email?token={}&register=True".format(create_verify_email[0].token)
        recepient = "{}".format(instance.email)
        send_mail(subject,message,settings.EMAIL_HOST_USER, [recepient],fail_silently=True)
