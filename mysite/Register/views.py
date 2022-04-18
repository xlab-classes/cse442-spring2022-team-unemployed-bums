from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def register(response):
    #Creating A New User 
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(response, "Account has been created for " + user)
            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})



def authenticated(response):
    return render(response, "registration/authenticated.html", {})

def registered(response):
    return render(response, "registration/registered.html", {})

