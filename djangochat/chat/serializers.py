
from .models import *
from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'