from django.urls import path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    path('ws/chat/<str:room>',ChatConsumer.as_asgi()),
]