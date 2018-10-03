from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .api import VoleibalistViewSet, EventViewSet

router = DefaultRouter()
router.register("voleibalists", VoleibalistViewSet)
router.register("events", EventViewSet)

urlpatterns = [

] + router.urls