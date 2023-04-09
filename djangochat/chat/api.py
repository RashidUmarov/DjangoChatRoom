from .models import *
from rest_framework import viewsets, permissions
from .serializers import RoomSerializer,MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [
        #permissions.AllowAny
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [
        #permissions.AllowAny
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = MessageSerializer