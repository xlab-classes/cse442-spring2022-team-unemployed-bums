from ast import Pass
import re
from django.shortcuts import redirect, render
from django.views import View
from .models import Follow
from django.contrib.auth.models import User
from listingcreation.views import ListingCreationModel

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

def deleteAccount(request):
    if request.method == 'GET':
        if User.objects.filter(username=request.GET.get('user')).exists():   
            #deleteMe = User.objects.get(username = request.GET.get('user'))
            #deleteMe.delete()
            print("exists ... remove the comments to test deletion")
            return render(request, 'profileHome/deleteAccount.html')
        else:
            print("Account doesn't exist")


class Index(View):
    #def profile(request):
    def get(self, request, *args, **kwargs):
        resp_following = request.GET.get('user')
        resp_follower = request.user.username

        if resp_follower == "":
            return render(request, 'profileHome/profile.html')

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
            return render(request, 'profileHome/profile.html', context)
        else:
            return render(request, 'profileHome/user_not_found.html')
