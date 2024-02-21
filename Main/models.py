from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todolist(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE,default="None",related_name="owner")
    users = models.ManyToManyField(to=User,default="None")
    name = models.CharField(max_length=200)

class Listitem(models.Model):

    name = models.CharField(max_length=200)
    list = models.ForeignKey(to=Todolist,on_delete=models.CASCADE)
    done = models.BooleanField()

class Message(models.Model):
    text = models.CharField(max_length=500)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    time = models.DateTimeField(name="datetime")
    todolist = models.ForeignKey(to=Todolist, on_delete=models.CASCADE)