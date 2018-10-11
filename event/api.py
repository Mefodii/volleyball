from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounting.serializers import PaymentSerializer

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


@api_view(['POST'])
def add_event(request):
    if request.method == 'POST':
        payments = request.data["payments"]
        request.data["payments"] = []
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event = event_serializer.save()
            for value in payments:
                value["event_id"] = event.id
            payment_serializer = PaymentSerializer(data=payments, many=True)
            if payment_serializer.is_valid():
                payments_instance = payment_serializer.save()
                event.payments.add(*payments_instance)
                return Response(request.data, status=status.HTTP_202_ACCEPTED)
            else:
                event.delete()
                return Response(payment_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(event_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)