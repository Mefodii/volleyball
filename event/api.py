from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounting.serializers import PaymentSerializer
from accounting.models import Payment

from .models import Voleibalist, Event
from .serializers import VoleibalistSerializer, EventSerializer


class EventList(APIView):

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        payments = request.data["payments"]
        request.data["payments"] = []
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event = event_serializer.save()
            for value in payments:
                value["event_id"] = event.id
            payment_serializer = PaymentSerializer(data=payments, many=True)
            if payment_serializer.is_valid():
                payment_serializer.save()
                return Response(request.data, status=status.HTTP_201_CREATED)
            else:
                event.delete()
                return Response(payment_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(event_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class EventDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        payments = request.data["payments"]
        request.data["payments"] = []
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            payments_serializers = []
            payments_id = []
            for value in payments:
                if value["id"]:
                    payments_ids.append(value["id"])

            Payment.objects.filter(pk__in=payments_id)


            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VoleibalistViewSet(ModelViewSet):
    queryset = Voleibalist.objects.all()
    serializer_class = VoleibalistSerializer
    # permission_classes = (permissions.IsAuthenticated,)
