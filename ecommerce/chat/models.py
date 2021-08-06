from os import name
from django.db import models
from django.db.models.base import Model
from backend.models import User


class Room(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    users=models.ManyToManyField(User)

class Chat(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,blank=True,null=True)
    message=models.TextField()

    def __str__(self):
        return str(self.id)
