from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

#removed lines from contact function
""" 
    def contact(request):   
        if request.method == 'POST':
        form = listingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            searchTags = form.cleaned_data['searchTags']

    form = listingForm()"""

#snipperform function
"""def snipper_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            #title = form.cleaned_data['title']
            #description = form.cleaned_data['description']
            #searchTags = form.cleaned_data['searchTags']
            form.save()

    form = SnippetForm()
    return render(request, 'form.html', {'form': listingForm})"""

@csrf_exempt
def listingsubmission(request):
    return redirect('http://127.0.0.1:8000/home/')

@csrf_exempt
def creationpage(request):
    return render(request, 'listingcreationform.html')