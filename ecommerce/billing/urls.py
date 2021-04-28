from django.urls import path
from .views import *

urlpatterns = [
    path('api/billingprofile/',BillingProfileViews.as_view()),
    path('api/cards/',CardViews.as_view()),
]