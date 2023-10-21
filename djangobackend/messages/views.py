from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .models import Message
from .serializer import MessagesSerializerList, MessagesSerializerCreate, MessageSerializerDelete, MessageSerializerUpdate


class MessagesListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializerList


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializerCreate


class MessageDeleteView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializerDelete


class MessageUpdateView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializerUpdate
