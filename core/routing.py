from django.urls import path , include
from core.consumers import ChatConsumer

websocket_urlpatterns = [
    path("" , ChatConsumer.as_asgi()),
    ]