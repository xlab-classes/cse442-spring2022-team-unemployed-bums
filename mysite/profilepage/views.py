from email.policy import HTTP
from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Idk(View):
    def get(self, request, *args, **kwargs):
        return render(request,'profileHome/editProfile.html')

class Index(View):
    #def profile(request):
    def get(self, request, *args, **kwargs):
        return render(request, 'profileHome/profile.html')

# Create your views here.
    #return render_to_response('profileHome/editProfile.html')
