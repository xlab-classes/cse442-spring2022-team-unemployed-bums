from asyncio.windows_events import NULL
from msilib.schema import CompLocator
from tkinter import Image
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import profilePicCounter, profiles
from django.views.decorators.csrf import csrf_exempt
import os.path
import shutil

from .forms import *

def profile(request):
    return render(request, 'profileHome/profile.html')

@csrf_exempt
def editProfilePic(request):
    #counter = profilePicCounter()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'profileHome/pictureUpload.html', {'form' : form})

def success(request):
    return HttpResponse('successfully uploaded')

@csrf_exempt
def editProfile(request):
    

    basepath = os.getcwd()
    print("HOME BASE = ", basepath)
    if request.method == 'POST':
        
        if profiles.testfield:  #this works through the user login page because it saves the user's password on successful login then accesses 
                                #their data table to update their information
            individual = profiles()
           
            if profiles.objects.filter(testfield=profiles.testfield).exists():
                individual.testfield = profiles.objects.get(testfield=profiles.testfield)#I think this should work
                #when this if statement gets working duplicate everything in the else statement
                #into here (except small changes)
            else:
                individual.testfield = "no password"
                individual.username = request.POST['username']
                individual.bio = request.POST['bio']
                individual.interests = request.POST['interests']

                
            infoUpdate = profiles(username=individual.username, bio=individual.bio, interests=individual.interests)
            infoUpdate.save()

    return render(request, 'profileHome/editProfile.html', {})

#documentation says that the database will be updated based on certain things already being inside the database:
        #the process for that should be to make an object of the class
        #retrieve the user's information based and put it all in the object 
        #then change a field using the . operator
        #...i think

#Ideas on how to make it dynamic:
    #save the user's login and password when they login/register
    #this will be so that when they change their username, bio, interests or profile pic it will update the same field instead of making a completely separate one
    
        #1. can do django sessions variables(lot of research)
        #2. could do an import inside of here or inside of the registration page that saves the info the user put into a variable