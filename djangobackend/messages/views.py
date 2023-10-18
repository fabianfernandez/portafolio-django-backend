from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Message
from .serializer import MessagesSerializerList, MessagesSerializerCreate


class MessagesListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializerList


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializerCreate
