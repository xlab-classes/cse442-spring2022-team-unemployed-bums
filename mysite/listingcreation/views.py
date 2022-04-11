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
            eventdate = f"{eventmonth}/{eventday}/{eventyear}"
            l = ListingCreationModel(title=title, author=author, description=description, outdoors=outdoors, sports=sports, recreation=recreation, learning=learning, eventdate=eventdate)
            l.save()


    return redirect('/home')

@csrf_exempt
def creationpage(request):
    form = CreateNewListing
    return render(request, 'listingcreationform.html', {"form":form})