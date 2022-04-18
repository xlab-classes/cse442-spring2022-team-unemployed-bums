from django.shortcuts import render
from django.views import View
from listingcreation.views import ListingCreationModel

# Dummy data

# Create your views here.

listings = ListingCreationModel.objects.all()

class Index(View):
    #def profile(request):
    def get(self, request, *args, **kwargs):
        context = {
            'listings': []
        }
        if request.user != 'AnonymousUser':
            profile_listings = listings.filter(author=request.user)
            context = {
            'listings': profile_listings.values()
            }
        return render(request, 'profileHome/profile.html', context)
