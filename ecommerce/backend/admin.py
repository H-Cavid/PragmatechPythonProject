from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserVerify)
admin.site.register(UserOtp)
admin.site.register(User)
admin.site.register(UserAddress)