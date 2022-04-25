from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileForm
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

def userprofile(response):
    return render(response, "registration/profile.html", {})


def profile(response):
    if response.method == 'POST':
        user_form = UserUpdateForm(response.POST, instance=response.user)
        profile_form = ProfileForm(response.POST,
                                   response.FILES,
                                   instance=response.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(response, 'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=response.user)
        profile_form = ProfileForm(instance=response.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(response,'registration/edit_profile.html', context)


