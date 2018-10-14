from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .api import VoleibalistViewSet, EventList, EventDetail

router = DefaultRouter()
router.register("voleibalists", VoleibalistViewSet)

urlpatterns = [
    path("events/", EventList.as_view()),
    path("events/<int:pk>/", EventDetail.as_view()),
] + router.urls