from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
class Registration(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email","password1","password2"]

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