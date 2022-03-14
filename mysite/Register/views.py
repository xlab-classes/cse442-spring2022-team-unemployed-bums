from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

# Create your views here.
def register(response):
    #Creating A New User 
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/registered")
    else:
        form = UserCreationForm()

    return render(response, "Register/register.html", {"form": form})

def authenticated(response):
    return render(response, "Register/authenticated.html", {})

def registered(response):
    return render(response, "Register/registered.html", {})

