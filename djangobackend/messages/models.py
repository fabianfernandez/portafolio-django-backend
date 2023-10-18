from django.db import models


class Message(models.Model):
    sender = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
