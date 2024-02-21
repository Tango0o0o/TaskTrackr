from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from .forms import Registration, ProfileForm, DateForm
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.

def register(req):
    if req.method == "GET":
        form = Registration()
        return render(req, "registration/register.html", {"form":form})
    else:
        new_user = Registration(req.POST)
        if new_user.is_valid():
            user = new_user.save()
            login_user(req, user)
        else:
            return redirect("/register/")
        return redirect(f"{reverse('edit_profile')}")

def edit_profile(req):
    
    if req.method == "GET":
        day = datetime.date.today().day
        month = datetime.date.today().month
        if month < 10:
            month = "0" + str(month)
        
        if day < 10:
            day = "0" + str(day)
            
        year = datetime.date.today().year
        form = DateForm(data={"date":f"{month}/{day}/{year} 4:37 PM"})
        profile_form = ProfileForm(instance=req.user.profile)
        return render(req, "Users/edit_profile.html",{"profile_form":profile_form, "form":form})
    else:
     
        
        profile_form = ProfileForm(req.POST,req.FILES,instance=req.user.profile)
        if profile_form.is_valid():
            profile = profile_form.save()
            dob = req.POST["date"]
            print(dob)
            # ['09/22/2023 4:37 PM']
            dob = f"{dob[6:10]}-{dob[0:2]}-{dob[3:5]}"
            profile.DOB = dob
            profile.save()
            return redirect(f"{reverse('edit_profile')}")
        else:
            print(profile_form.errors.as_data())
    
    return redirect("/")

def view_profile(req,user_id):
    user = User.objects.get(id=user_id)
    return render(req, "Users/profile.html", {"user_":user})

@csrf_exempt
def discord_login(req):
    id = req.POST.get('id')
    code = req.POST.get('code')
    user = User.objects.get(id=id)

    if int(code) == int(user.profile.code):
        print("s")
        return HttpResponse(content="True")
    else:
        return HttpResponse(content="False")