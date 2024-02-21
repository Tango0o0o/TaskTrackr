from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from random import choice
from django.conf.urls.static import static
from datetime import date
from PIL import Image
from random import randint
import os
# Create your models here.

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

class Profile(models.Model):
    
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, name="user")
    image = models.ImageField(name="profile_pic",default="default_pics/other.png",upload_to="profile_pics")
    dob = models.DateField(name="DOB",default=date(1990,1,1))
    gender = models.CharField(choices=gender_choices,default="Male",max_length=10,name="gender")
    code = models.IntegerField(name="code", default=randint(10000000, 99999999))
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path)
        img.thumbnail((300, 300))
        img.save(f"media/profile_pics/{str(self.user.id)}.png")
        