from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Voleibalist, Event
from .serializers import VoleibalistSerializer, EventSerializer


class VoleibalistViewSet(ModelViewSet):
    queryset = Voleibalist.objects.all()
    serializer_class = VoleibalistSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = (permissions.IsAuthenticated,)
