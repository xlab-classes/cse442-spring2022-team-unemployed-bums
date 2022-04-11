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
            description = form.cleaned_data["description"]
            outdoors = form.cleaned_data["outdoors"]
            sports = form.cleaned_data["sports"]
            recreation = form.cleaned_data["recreation"]
            learning = form.cleaned_data["learning"]
            l = ListingCreationModel(title=title, description=description, outdoors=outdoors, sports=sports, recreation=recreation, learning=learning)
            l.save()


    return redirect('http://127.0.0.1:8000/home/')

@csrf_exempt
def creationpage(request):
    form = CreateNewListing
    return render(request, 'listingcreationform.html', {"form":form})