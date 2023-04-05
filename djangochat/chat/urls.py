from django.urls import path, include
from . import views

from rest_framework import routers
from .api import RoomViewSet, MessageViewSet

router=routers.DefaultRouter()
router.register('rooms',RoomViewSet,'rooms')
router.register('messages',MessageViewSet,'messages')

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]