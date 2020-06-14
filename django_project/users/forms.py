from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm      # inbuld user form
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()      # adding email field
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        # sequence of form(way of display)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User        # model is what go as output
        fields = ['username', 'email'] 


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile         # model is what go as output
        fields = ['image']