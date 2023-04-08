from django.urls import path, include
from . import views

from rest_framework import routers
from .api import RoomViewSet, MessageViewSet

router=routers.DefaultRouter()
router.register('rooms',RoomViewSet,'rooms')
router.register('messages',MessageViewSet,'messages')

urlpatterns = [
    path('', views.home, name='home'),   # выбор комнаты для чата на запросах XMLHttpRequest
    path('api/', include(router.urls)),
    path("choose", views.index, name="index"),    # выбор комнаты с чатом на websocket
    path("choose/<str:room_name>/", views.newroom, name="newroom"), # вид комнаты с чатом на websocket
    path('<str:room>/', views.room, name='room'), # чат на запросах XMLHttpRequest каждую секунду
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]