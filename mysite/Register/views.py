from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.views import View
from .models import Follow
from django.contrib.auth.models import User
from listingcreation.views import ListingCreationModel

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

def userprofile(request):
    resp_following = request.GET.get('user')
    resp_follower = request.user.username

    if resp_follower == "":
        return render(request, 'registration/profile.html')

    if User.objects.filter(username=resp_following).exists():
        following = User.objects.get(username=resp_following)
        follower = User.objects.get(username=resp_follower)

        is_following = Follow.objects.filter(user=follower, following_user=following).exists()

        listings = ListingCreationModel.objects.filter(author=resp_following)
        
        context = {
        'listings': listings,
        'following': following,
        'follower': follower,
        'is_following': is_following,
        }
        return render(request, 'registration/profile.html', context)
    else:
        return render(request, 'profileHome/user_not_found.html')
# return render(response, "registration/profile.html", {})


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

# Create your views here.
def remove_follower(request):
    if request.method == 'POST':
    
        resp = dict(list(request.POST.items()))
        resp_follower = resp['follower']
        resp_following = resp['following']

        if User.objects.filter(username=resp_following).exists():
            following = User.objects.get(username=resp_following)
            follower = User.objects.get(username=resp_follower)
            if Follow.objects.filter(following_user=following, user=follower).exists():
                removeFollow = Follow.objects.get(user=follower, following_user=following)
                print("Deleted follow object: {}".format(removeFollow))
                removeFollow.delete()
    return redirect('/profile/?user=' + resp_following)

def add_follower(request):
    if request.method == 'POST':
        resp = dict(list(request.POST.items()))
        resp_follower = resp['follower']
        resp_following = resp['following']

        if User.objects.filter(username=resp_following).exists():
            following = User.objects.get(username=resp_following)
            follower = User.objects.get(username=resp_follower)

            if following != follower:
                try:
                    follow = Follow.objects.create(user=follower, following_user=following)
                    print("Saved follow object: {}".format(follow))
                    follow.save()
                except Exception as e:
                    print("Failed to create follow object: {}".format(e))
            else:
                print("Cannot follow self")
        else:
            print("User does not exist: {}".format(resp_following))

    return redirect('/profile/?user=' + resp_following)

# class Index(View):
#     #def profile(request):
#     def get(self, request, *args, **kwargs):
#         resp_following = request.GET.get('user')
#         resp_follower = request.user.username

#         if resp_follower == "":
#             return render(request, 'registration/profile.html/profile.html')

#         if User.objects.filter(username=resp_following).exists():
#             following = User.objects.get(username=resp_following)
#             follower = User.objects.get(username=resp_follower)

#             is_following = Follow.objects.filter(user=follower, following_user=following).exists()

#             listings = ListingCreationModel.objects.filter(author=resp_following)
            
#             context = {
#             'listings': listings,
#             'following': following,
#             'follower': follower,
#             'is_following': is_following,
#             }
#             return render(request, 'R/profile.html', context)
#         else:
#             return render(request, 'profileHome/user_not_found.html')
