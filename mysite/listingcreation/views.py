from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateNewListing
from .models import ListingCreationModel

@csrf_exempt
def listingsubmission(request):
    if request.method == "POST":
        form = CreateNewListing(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            author = request.user
            description = form.cleaned_data["description"]
            outdoors = form.cleaned_data["outdoors"]
            sports = form.cleaned_data["sports"]
            recreation = form.cleaned_data["recreation"]
            learning = form.cleaned_data["learning"]
            eventday = form.cleaned_data["eventday"]
            eventmonth = form.cleaned_data["eventmonth"]
            eventyear = form.cleaned_data["eventyear"]
            eventdate = "{} {} {}".format(eventmonth, eventday, eventyear)
            print(request.user)
            l = ListingCreationModel(title=title, author=author, description=description, outdoors=outdoors, sports=sports, recreation=recreation, learning=learning, eventdate=eventdate)
            l.save()


    return redirect('/home')

@csrf_exempt
def creationpage(request):
    form = CreateNewListing
    return render(request, 'listingcreationform.html', {"form":form})

@csrf_exempt
def hidepost(request):
    listings = ListingCreationModel.objects.all().values()
    items = dict(list(request.POST.items()))
    listing = listings.get(id=int(items['listing_id']))
    hidden = listing["hidden"]
    print("post visibility before: " , hidden)
    print("hidden type: " , type(hidden))
    if(hidden == False):
        ListingCreationModel.objects.filter(pk=int(items['listing_id'])).update(hidden="True")
        print("hiding")
    else:
        ListingCreationModel.objects.filter(pk=int(items['listing_id'])).update(hidden="False")
        print("showing")
    newlistings = ListingCreationModel.objects.all().values()
    newlisting = newlistings.get(id=int(items['listing_id']))
    print("post visibility after: ", newlisting["hidden"])
    return redirect('/home')

def rsvp(request):
    listings = ListingCreationModel.objects.all().values()
    items = dict(list(request.POST.items()))
    listing = listings.get(id=int(items['listing_id']))
    count = int(listing["rsvp"]) + 1
    ListingCreationModel.objects.filter(pk=int(items['listing_id'])).update(rsvp=count)
    return None