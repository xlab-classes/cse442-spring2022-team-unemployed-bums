from cgitb import html
from email import message
from tokenize import String
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from listingcreation.views import ListingCreationModel
from .forms import Tagsform
from django.views.decorators.csrf import csrf_exempt
from listingcreation.views import rsvp
from operator import itemgetter
import operator

# Create your views here.

listings = ListingCreationModel.objects.all()

def get_event_info(username, listing_id):
    
    listing = listings.get(id=int(listing_id))
    print(f"listing: {type(listing)}")

    if listing:
        author = listing.author.username
        title = listing.title
        content = listing.description
        eventdate = listing.eventdate

        return (
            "Thank you for the RSVP {}!\nYou have RSVP'd to {} - posted by {}\n\nDescription\n{}\n\nEvent Date {}\nEVNT RSVP Notifications".format(username, title, author, content, eventdate)
        )
        


    return 'this is the event info'

def index(request):
    list_of_listings = ListingCreationModel.objects.all()
    form = Tagsform
    final_listings = []
    for listing in list_of_listings:
        if (listing.hidden == False):
            final_listings.append(listing)

    context = {
        'listings': final_listings,
        'tagsform': form,
        'message': "",
    }

    if request.method == 'GET':
        return render(request, 'home/index.html', context)
    else:
        if str(request.user) != "AnonymousUser":
            items = dict(list(request.POST.items()))
            print(items)
            key, value = items
            # send email to user here
            # send_mail(get_event_info(request.user, items['listing_id']))
            send_mail(
                subject='You RSVP\'d to an event!',
                message=get_event_info(request.user, items['listing_id']),
                from_email='EVNT RSVP',
                recipient_list=[request.user.email],
            )
            context['message'] = "Successful RSVP"
            print(key, value, "sending rsvp email")
        else:
            context['message'] = "You must log in to RSVP"
        return render(request, 'home/index.html', context)

@csrf_exempt
def filtered(request):
    list_of_listings = ListingCreationModel.objects.all().values()
    final_listings = []

    form = Tagsform
    if request.method == "POST":
        form = Tagsform(request.POST)

        if form.is_valid():
            outdoors = form.cleaned_data["outdoors"]
            sports = form.cleaned_data["sports"]
            recreation = form.cleaned_data["recreation"]
            learning = form.cleaned_data["learning"]
            sort = form.cleaned_data["sortOption"]

            for listing in list_of_listings:
                if (listing["hidden"] == False):
                    outd = False
                    sport = False
                    rec = False
                    learn = False
                    if(outdoors == False and sports == False and recreation == False and learning == False):
                        final_listings.append(listing)
                    else:
                        if(outdoors == True):
                            if (listing["outdoors"] == outdoors):
                                outd = True
                        else:
                            outd = True
                        if (sports == True):
                            if (listing["sports"] == sports):
                                sport = True
                        else:
                            sport = True
                        if (recreation == True):
                            if (listing["recreation"] == recreation):
                                recreation = True
                        else:
                            rec = True
                        if (learning == True):
                            if (listing["learning"] == learning):
                                learn = True
                        else:
                            learn = True
                        if(outd == True and sport == True and rec == True and learn == True):
                            final_listings.append(listing)
        if (sort == "mostpopular"):
            final_listings.sort(key=itemgetter('rsvp'))
        elif (sort == "leastpopular"):
            final_listings.sort(key=itemgetter('rsvp'), reverse=True)

        context = {
            'listings': final_listings,
            'tagsform': form
        }
        return render(request, 'home/index.html', context)

    else:
        context2 = {
            'listings': list_of_listings,
            'tagsform': form
        }
        return render(request, 'home/index.html', context2)
