from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Todolist, Listitem, Message
from django.http import HttpResponse
from django.contrib.auth.models import User
from Users.forms import ProfileForm
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def validate_owned_list(user, id):

    todo_list = Todolist.objects.get(id=id)
    if user in todo_list.users.all():
        return [True, todo_list]
    else:
        return [False]

def home(req):
    return render(req, "Main/home.html")

def save_list(req, saved_id):
    validation = validate_owned_list(req.user, saved_id)
    if saved_id and validation[0] == True and req.method == "POST":
        list = validation[1]
        list.name = req.POST["list-name"]
        list.save()
        return redirect(f"{reverse('save_list', kwargs={'saved_id':list.id})}")
    else:
        user_lists = Todolist.objects.filter(users=req.user)
        return render(req, "Main/my_lists.html",{"lists":user_lists, "saved_id":saved_id})

def my_lists(req):
    user_lists = Todolist.objects.filter(users=req.user)
    return render(req, "Main/my_lists.html",{"lists":user_lists})

@csrf_exempt
def create_list(req):
    if req.POST["discord"]:
        user = User.objects.get(id=req.POST["id"])
        name = req.POST["list-name"]
        new_list = Todolist(name=name, owner=user)
        new_list.save()
        new_list.users.add(user)
        return HttpResponse(content=True)


    if req.method == "GET":
        return redirect(f"{reverse('my_lists')}")
    else:
        name = req.POST["list-name"]
        new_list = Todolist(name=name, owner=req.user)
        new_list.save()
        new_list.users.add(req.user)
        return redirect(f"{reverse('my_lists')}")
    
    
def delete_list(req, id):
    validation = validate_owned_list(req.user, id)
    if not id or validation[0] == False:
        return redirect(f"{reverse('my-lists')}")
    else:
        list = validation[1]
        list.delete()
        return redirect(f"{reverse('my_lists')}")

def add_user(req, list_id):
    validation = validate_owned_list(req.user, list_id)
    if list_id and validation[0] == True and req.method == "POST":
        username = req.POST["username"]
        user = User.objects.get(username=username)
        todo_list = validation[1]
        todo_list.users.add(user)
        return redirect(f"{reverse('my_lists')}")
    else:
        return redirect(f"{reverse('my_lists')}")

def remove_user(req, list_id):
    validation = validate_owned_list(req.user, list_id)
    if list_id and validation[0] == True and req.method == "POST":
        username = req.POST["username"]
        user = User.objects.get(username=username)
        todo_list = validation[1]
        if todo_list.owner != user:
            todo_list.users.remove(user)
        return redirect(f"{reverse('my_lists')}")
    else:
        return redirect(f"{reverse('my_lists')}")

def remove_self(req, list_id):
    todo_list = Todolist.objects.get(id=list_id)
    todo_list.users.remove(req.user)
    return redirect(f"{reverse('shared_lists')}")


def my_list(req, list_id):
    validation = validate_owned_list(req.user, list_id)

    if list_id and validation[0] == True and req.method == "GET":
        return render(req, "Main/list.html",{"list":validation[1]})
    else:
        return redirect(f"{reverse('my_lists')}")

def create_item(req, list_id):
    validation = validate_owned_list(req.user, list_id)

    if list_id and validation[0] == True and req.method == "POST":
        item = Listitem(name=req.POST["item-name"],list=validation[1],done=False)
        item.save()

    return redirect(f"{reverse('my_list',kwargs={'list_id': list_id})}")

def edit_item(req, list_id, item_id):
    validation = validate_owned_list(req.user, list_id)
    if list_id and validation[0] == True and req.method == "POST":
        item = validation[1].listitem_set.get(id=item_id)
        item.name = req.POST["item-name"]
        item.save()
        return redirect(f"{reverse('my_list', kwargs={'list_id': list_id})}")

def delete_item(req, list_id, item_id):
    validation = validate_owned_list(req.user, list_id)
    if list_id and validation[0] == True:
        item = validation[1].listitem_set.get(id=item_id)
        item.delete()
        return redirect(f"{reverse('my_list', kwargs={'list_id': list_id})}")

def change_state(req, list_id, item_id, done):
    validation = validate_owned_list(req.user, list_id)

    if list_id and validation[0] == True:
        item = validation[1].listitem_set.get(id=item_id)
        if done == "False":
            item.done = False
        else:
            item.done = True
        item.save()

    return redirect(f"{reverse('my_list', kwargs={'list_id': list_id})}")

def shared_lists(req):

    user_lists = Todolist.objects.filter(users=req.user).exclude(owner=req.user)
    return render(req, "Main/shared_lists.html",{"lists":user_lists})

def send_message(req, list_id):
    validation = validate_owned_list(req.user, list_id)

    if list_id and validation[0] == True:
        message = Message(text=req.POST["message"],user=req.user,datetime=timezone.now(),todolist=validation[1])
        message.save()
        return redirect(f"{reverse('my_list', kwargs={'list_id': list_id})}")
    
def link_discord(req):
    if req.method == "GET":
        return render(req, "Main/discord.html")

