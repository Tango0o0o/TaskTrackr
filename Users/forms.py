from typing import Any
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

class Registration(UserCreationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None: # learn init fr
        super().__init__(*args, **kwargs)
        del self.fields["password2"] # wtf is thissssssss
        self.fields["username"].label = "Email" # Set the username to an email, less fields

        for field in self.fields:
            label = field.replace("_", " ").capitalize() # Changing the labels to be presentable e.g "first_name" to "First name"
            self.fields[field].widget.attrs = {"class" : "form-input interact", "label" : f"{label}"} # Setting css + html stuff

        self.fields["username"].widget.attrs.update({"type" : "email"})


    first_name = forms.CharField(max_length=50,label="First name", required=True)
    last_name = forms.CharField(max_length=50,label="Last name", required=False)


    class Meta:
        model = User
        fields = ["first_name", "last_name", "username","password1"]

class LoginForm(AuthenticationForm): # need to tweak login form a lil bit
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)

        self.fields["username"].label = "Email" # Change username to act as an email (still unique id)

        for field in self.fields:
            label = field.replace("_", " ").capitalize() # Changing the labels to be presentable e.g "first_name" to "First name"
            self.fields[field].widget.attrs = {"class" : "form-input interact", "label" : f"{label}"} # Setting css + html stuff


    class Meta:
        fields = ["username", "password"] #adding in the fields

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields = ["profile_pic", "gender"]

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )