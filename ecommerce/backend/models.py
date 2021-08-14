# from ecommerce.courier.models import STATUS
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
import jwt
from datetime import date, datetime, timedelta
from django.conf import settings
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
# from django.contrib.auth.backends import BaseBackend

#####
#Username elave etmek lazimdir
#Create super userde Username elave olunmalidir
#username yoxlanmalidi olub veya olmamasi
#username yazilmayanda error vermelidi

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email,user_name,first_name,date_of_birth=None, password=None,**other_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not user_name:
            raise ValueError("User_name must be given and unique please try again")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,user_name,first_name,date_of_birth=None, password=None,**other_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            user_name,
            first_name,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone=models.CharField(max_length=12)
    last_name=models.CharField(max_length=25)
    first_name=models.CharField(max_length=25)
    user_name = models.CharField(max_length=25,unique=True,blank=True) 
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    date_of_birth = models.DateField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']

    def __str__(self):
        return self.email
    
    def parse_data_log(self):
        return "ID-si:{} , AD-ı:{} , Soyad-ı:{} , Email-i:{}, nömrəsi:{} olan istifadəçi yaradıldı".format(self.id,self.first_name,self.last_name,self.email,self.phone)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


@receiver(post_save,sender=User)
def userprofile_parse(instance,created,*args,**kwargs):
    print(instance)
    if created is True:
    # print(instance.is_phone_status)
            log_data = instance.parse_data_log()
            Profile.objects.create(created_user_id=instance.id,log=log_data,first_name=instance.first_name,last_name=instance.last_name,user_phone_number=instance.phone,
            user_email=instance.email)


















class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address_name = models.CharField(max_length=40)
    home = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

    def __str__(self):
        return self.user.email




class UserOtp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_otp')
    otp = models.CharField(max_length=6)
    rpt = models.IntegerField(default=3)
    date = models.DateTimeField(auto_now=True)




class UserVerify(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    token = models.CharField(max_length=400,blank=True,null=True)
    status = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.token

    def save(self,*args, **kwargs):
        self.token = ''
        if not self.token:
            self.token = self._create_verify_token()
        super().save(*args, **kwargs)

    def _create_verify_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            "id": self.id,
            "exp": int(dt.timestamp())
        },settings.SECRET_KEY,algorithm='HS256')
        return token




class Profile(models.Model):
    created_user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    user_image = models.ImageField(upload_to='UserProfile_pictures', default='userprofile.jpg')
    user_balance = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True,default=0.00)
    user_links = models.CharField(max_length=50,blank=True,null=True)
    user_phone_number =  models.CharField(max_length=20)
    user_email = models.EmailField(max_length=20)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    log = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return str(self.user_email)





# class User(AbstractUser):
#     phone = models.IntegerField(blank=True, null=True)
#     is_branch = models.BooleanField(default=True)
#     is_delivery = models.BooleanField(default=True)
#     is_phone_status = models.BooleanField(default=False)

#     def parse_data_log(self):
#         return "ID-si:{} , AD-ı:{} , Soyad-ı:{} , Email-i:{}, nömrəsi:{} olan istifadəçi yaradıldı".format(self.id,self.first_name,self.last_name,self.email,self.phone)




# @receiver(post_save,sender=User)
# def userprofile_parse(instance,created,*args,**kwargs):
#     if created is True:
#     # print(instance.is_phone_status)
#         if instance.is_phone_status is True:
#             log_data = instance.parse_data_log()
#             Profile.objects.create(created_user_id=instance.id,log=log_data,first_name=instance.first_name,last_name=instance.last_name,user_phone_number=instance.phone,
#             user_email=instance.email)

# if instance.is_phone_status = 
    # print(instance.id)
    # print(instance.parse_data_log())
    # print(instance.first_name)
 # last_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='last_name_set')
    # user_email = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='email_set')
    # user_phone_number = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='phone_set')
    # first_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='first_name_set')
    # # user_phone = PhoneField(blank=True, help_text='Contact phone number')

#hasni field registerden kececekse mutleq sekilde unique=true



# class User(AbstractUser):
#     phone = models.IntegerField(blank=True, null=True)
#     is_branch = models.BooleanField(default=True)
#     is_delivery = models.BooleanField(default=True)
#     is_phone_status = models.BooleanField(default=False)

#     def parse_data_log(self):
#         return "ID-si:{} , AD-ı:{} , Soyad-ı:{} , Email-i:{}, nömrəsi:{} olan istifadəçi yaradıldı".format(self.id,self.first_name,self.last_name,self.email,self.phone)


# Create your models here.
# User qeydiyatdan kecende 
# User ucun userprofile adinda model yaratmaq lazimdir
# Profile modelin fieldsleri user-e bagli olmalidi avtomatik olaraq elave fieldleri olmalidi diger fieldlar olamlidi
# user image default her hansisa bir sekil verilmelidi
# User balance olmalidi
# User-in sosial linkleri olmalidi
# User modelden phone fields goturmelidi
# User modelden email goturmelidi
# Last name,first name
#userden inherit ele
# STATUS = (
#     ('ÇATDIRILDI','ÇATDIRILDI'),
#     ('YOLDADIR','YOLDADIR'),
# )