from rest_framework import serializers
from .models import Message


class MessagesSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class MessagesSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'subject', 'body']
