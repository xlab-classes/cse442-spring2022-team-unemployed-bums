from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateNewListing
from .models import ListingCreationModel
from django.contrib.auth.models import User
from django.core.mail import send_mail
from Register.views import Follow

def get_event_info(username, listing):

    if listing:
        author = listing.author.username
        title = listing.title
        content = listing.description
        eventdate = listing.eventdate

        return (
            "{} has posted a new event! Below is the event description:\n\n{}\nPosted by {}\n\n{}\n\nRSVP by {}".format(author, title, author, content, eventdate)
        )

@csrf_exempt
def listingsubmission(request):
    if request.method == "POST":
        form = CreateNewListing(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            author = User.objects.get(username=request.user)
            description = form.cleaned_data["description"]
            outdoors = form.cleaned_data["outdoors"]
            sports = form.cleaned_data["sports"]
            recreation = form.cleaned_data["recreation"]
            learning = form.cleaned_data["learning"]
            eventday = form.cleaned_data["eventday"]
            eventmonth = form.cleaned_data["eventmonth"]
            eventyear = form.cleaned_data["eventyear"]
            eventdate = "{} {} {}".format(eventmonth, eventday, eventyear)
            # print(request.user)
            l = ListingCreationModel(title=title, description=description, author=author, outdoors=outdoors, sports=sports, recreation=recreation, learning=learning, eventdate=eventdate)
            l.save()

            # send notification to followers
            follower_objects = Follow.objects.filter(following_user=User.objects.get(username=request.user))
            followers = []
            for follower_object in follower_objects:
                followers.append(User.objects.get(id=follower_object.user.id))
            print(followers)
            send_mail(
                subject="You followed {}, check out their latest post!".format(author),
                message=get_event_info(request.user, l),
                from_email="{} posted a new event!".format(author),
                recipient_list=[follower.email for follower in followers],
            )


    return redirect('/home')

@csrf_exempt
def creationpage(request):
    form = CreateNewListing
    return render(request, 'listingcreationform.html', {"form":form})