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

    return render(response, "Register/register.html", {"form": form})

def loginpage(response):
    if response.method == "POST":
        username = response.POST.get('username')
        password = response.POST.get('password')
        user = authenticate(response, username = username, password = password )
        if user is not None:
            login(response, user)
            return redirect("home")
        else:
            messages.info(response, "Username or Password is incorrect")
            return render(response, "Register/login.html")
    return render(response, "Register/login.html")


def authenticated(response):
    return render(response, "Register/authenticated.html", {})

def registered(response):
    return render(response, "Register/registered.html", {})

