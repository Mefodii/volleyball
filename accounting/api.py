from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from event.models import Event

from .models import Payment, Expense
from .serializers import PaymentSerializer, ExpenseSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        payment = serializer.save()
        event = Event.objects.get(pk=payment.event_id.id)
        event.payments.add(payment)
        event.save()


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # permission_classes = (permissions.IsAuthenticated,)
