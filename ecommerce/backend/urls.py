from .views import *
from django.urls import path
from .password_reset import ResetPasswordEmail,check_email,PasswordResetViwe

urlpatterns=[
    path("api/user/",UserDetail.as_view()),
    path("api/login/",LoginTokenView.as_view()),
    path("api/register/",RegisterViews.as_view()),
    path('api/reset/email',ResetPasswordEmail.as_view()),
    path('check_email/',check_email),
    path('api/password_reset/',PasswordResetViwe.as_view()),
]