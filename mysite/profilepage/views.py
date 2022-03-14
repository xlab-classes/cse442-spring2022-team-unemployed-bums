from django.shortcuts import render
from django.views import View

class Index(View):
    #def profile(request):
    def get(self, request, *args, **kwargs):
        return render(request, 'profileHome/profile.html')
# Create your views here.
