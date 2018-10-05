from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .api import PaymentViewSet, ExpenseViewSet

router = DefaultRouter()
router.register("payments", PaymentViewSet)
router.register("expenses", ExpenseViewSet)

urlpatterns = [

] + router.urls