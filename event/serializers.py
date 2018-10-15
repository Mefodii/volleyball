from rest_framework import serializers

from .models import Voleibalist, Event
from accounting.serializers import PaymentSerializer


class VoleibalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voleibalist
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField()

    def get_payments(self, instance):
        payments = instance.payment_set.all()
        return PaymentSerializer(payments, many=True).data

    class Meta:
        model = Event
        fields = '__all__'
