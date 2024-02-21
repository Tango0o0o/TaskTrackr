from django.contrib import admin
from .models import Todolist, Listitem, Message
# Register your models here.

admin.site.register(Todolist)
admin.site.register(Listitem)
admin.site.register(Message)