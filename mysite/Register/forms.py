from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from .models import Profile 


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField 
    class Meta:
        model = User 
        fields = ['username', 'email']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']