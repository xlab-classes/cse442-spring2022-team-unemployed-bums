from cgitb import html
from email import message
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from listingcreation.views import ListingCreationModel
from .forms import Tagsform

# Create your views here.

# Dummy data
# listings = [
#     {   
#         'id': '8271928371',
#         'author': 'Abe',
#         'title': 'Soccer Event',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed gravida a erat vitae luctus. Nullam in ipsum quis velit viverra malesuada. Cras quis pharetra massa. Donec vehicula, mauris at congue sollicitudin, nisi ante porttitor odio, iaculis lacinia nisi lacus dignissim tortor. Donec justo lacus, pretium nec leo eu, dictum tincidunt elit. Vivamus a mi eu nunc cursus maximus. Duis sed lacinia nisl. Aliquam lobortis sapien at orci dictum efficitur. Aenean vel maximus tellus. Fusce a rhoncus magna. Proin venenatis ipsum diam. Donec nunc velit, vehicula a imperdiet eget, congue a odio. Donec ullamcorper nec eros facilisis rutrum. Aliquam hendrerit aliquet lectus nec mollis. Vestibulum eu orci maximus, vehicula sem ut, efficitur nisl.',
#         'date_posted': '03/13/2022',
#         'event_date': '04/01/2022'
#     },
#     {
#         'id': '1830293816',
#         'author': 'Simon',
#         'title': 'Chess Club',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec dictum enim risus, nec finibus urna mollis sit amet. Donec facilisis hendrerit neque, et malesuada massa facilisis dictum. In ultrices, ex quis fermentum vulputate, diam lacus luctus leo, vel ullamcorper turpis mi vel nunc. Integer viverra neque sit amet nunc dignissim lacinia. Donec pretium lacinia sapien, a placerat tortor bibendum vitae. Phasellus a faucibus elit, eget faucibus odio. Suspendisse interdum pretium orci, vel fermentum felis vestibulum et. Sed at interdum libero, et pellentesque metus. Duis dictum est eget venenatis commodo.',
#         'date_posted': '03/13/2022',
#         'event_date': '04/12/2022'
#     },
#     {
#         'id': '6291049820',
#         'author': 'John',
#         'title': 'Basketball Tournament',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vitae enim condimentum, commodo ex nec, gravida libero. Duis quis libero efficitur, malesuada diam vitae, posuere erat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In id lectus mollis diam auctor venenatis vel non urna. Praesent vehicula nibh justo, eget pharetra quam luctus ut. Proin laoreet, arcu at posuere ultrices, ipsum neque viverra mauris, ac malesuada mauris purus et velit. Nulla non molestie enim. Proin bibendum ut mi gravida pretium. Nunc volutpat eu tellus consectetur egestas. Praesent ultricies congue neque, quis interdum ipsum rhoncus eget. Donec volutpat tellus a magna commodo vestibulum. Etiam ornare ex nunc, ut eleifend ante aliquet vel. Aenean eget consequat sapien. Morbi viverra laoreet turpis ut aliquam. Aliquam et finibus augue. Donec ac tellus nulla.',
#         'date_posted': '03/13/2022',
#         'event_date': '05/15/2022'
#     },
#     {
#         'id': '5172261937',
#         'author': 'Samantha',
#         'title': 'Halloween Festival',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vitae enim condimentum, commodo ex nec, gravida libero. Duis quis libero efficitur, malesuada diam vitae, posuere erat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In id lectus mollis diam auctor venenatis vel non urna. Praesent vehicula nibh justo, eget pharetra quam luctus ut. Proin laoreet, arcu at posuere ultrices, ipsum neque viverra mauris, ac malesuada mauris purus et velit. Nulla non molestie enim. Proin bibendum ut mi gravida pretium. Nunc volutpat eu tellus consectetur egestas. Praesent ultricies congue neque, quis interdum ipsum rhoncus eget. Donec volutpat tellus a magna commodo vestibulum. Etiam ornare ex nunc, ut eleifend ante aliquet vel. Aenean eget consequat sapien. Morbi viverra laoreet turpis ut aliquam. Aliquam et finibus augue. Donec ac tellus nulla.',
#         'date_posted': '03/13/2022',
#         'event_date': '08/31/2022'
#     },
#     {
#         'id': '9810366282',
#         'author': 'Felix',
#         'title': 'Charlie\'s Birthday!!!',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vitae enim condimentum, commodo ex nec, gravida libero. Duis quis libero efficitur, malesuada diam vitae, posuere erat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In id lectus mollis diam auctor venenatis vel non urna. Praesent vehicula nibh justo, eget pharetra quam luctus ut. Proin laoreet, arcu at posuere ultrices, ipsum neque viverra mauris, ac malesuada mauris purus et velit. Nulla non molestie enim. Proin bibendum ut mi gravida pretium. Nunc volutpat eu tellus consectetur egestas. Praesent ultricies congue neque, quis interdum ipsum rhoncus eget. Donec volutpat tellus a magna commodo vestibulum. Etiam ornare ex nunc, ut eleifend ante aliquet vel. Aenean eget consequat sapien. Morbi viverra laoreet turpis ut aliquam. Aliquam et finibus augue. Donec ac tellus nulla.',
#         'date_posted': '03/13/2022',
#         'event_date': '03/14/2022'
#     },
#     {
#         'id': '3462918370',
#         'author': "Ursulina",
#         'title': "Ben's Barbeque",
#         'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed egestas nec sem at mattis. Vivamus cursus dolor sit amet nibh finibus, nec fringilla erat finibus. Nam pellentesque arcu eget purus varius aliquet. Fusce ornare eget diam vel elementum. Fusce tincidunt id eros ut congue. Suspendisse vulputate ut tortor vitae lacinia. Mauris urna nulla, semper vitae mauris sit amet, pretium iaculis ligula. Nunc et est tristique, condimentum tellus vulputate, pharetra ipsum.",
#         'date_posted': "03/13/2022",
#         'event_date': "08-10-22"
#     },
#     {
#         'id': '1293827209',
#         'author': "Jean",
#         'title': "Movie Night (FREE FOOD)",
#         'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed maximus dolor nibh. Nullam sit amet turpis at sapien tempor eleifend. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aliquam sodales vulputate enim interdum feugiat. Sed vitae fermentum magna. Fusce rhoncus est orci, non sollicitudin tortor mollis ut. Praesent consectetur ultricies leo vitae tincidunt. Pellentesque ultrices, quam eu aliquam scelerisque, sapien mi tincidunt felis, et aliquam justo arcu vitae nisl. Nulla lorem leo, facilisis sed sagittis eget, egestas vitae augue. In hac habitasse platea dictumst. Nulla quis nunc mi. Maecenas in sollicitudin elit.",
#         'date_posted': "03/13/2022",
#         'event_date': "12-16-22"
#     },
# ]
listings = ListingCreationModel.objects.all().values()

# def get_listing(listing_id):
#     listings = ListingCreationModel.objects.all.values()
#     for listing in listings:
#         print(listing)
#         if listing['id'] == listing_id:
#             return listing
#     return None

def get_event_info(username, listing_id):
    
    listing = listings.get(id=int(listing_id))
    print(listing)
    if listing:
        author = listing['author']
        title = listing['title']
        content = listing['description']
        eventdate = "temp date placeholder"

        return (
            f"""Thank you for the RSVP {username}!\n
You have RSVP'd to "{title}" - posted by {author}\n
\n
Description\n
{content}\n
\n
Event Date {eventdate}

EVNT RSVP Notifications
            """
        )
        


    return 'this is the event info'

def index(request):
    list_of_listings = ListingCreationModel.objects.all().values()
    form = Tagsform
    # print(list(context))
    context = {
        'listings': list_of_listings,
        'tagsform': form
    }
    # context = {
    #         'listings': listings
    #     }
    # current_user = request.user.email
    # print(current_user)
    if request.method == 'GET':
        return render(request, 'home/index.html', context)
    else:
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
        print(key, value, "sending rsvp email")
        return render(request, 'home/index.html', context)