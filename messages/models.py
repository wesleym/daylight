from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="messages_sent")
    recipient = models.ForeignKey(User, related_name="messages_received")
    message = models.TextField()