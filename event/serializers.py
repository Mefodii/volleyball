from rest_framework import serializers

from .models import Voleibalist, Event


class VoleibalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voleibalist
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
