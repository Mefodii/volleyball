from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .api import VoleibalistViewSet, EventViewSet, add_event

router = DefaultRouter()
router.register("voleibalists", VoleibalistViewSet)
router.register("events", EventViewSet)

urlpatterns = [
    path("add_event/", add_event),
] + router.urls