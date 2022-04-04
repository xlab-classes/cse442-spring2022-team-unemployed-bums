from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewList
# Create your views here.

def home(response):
    return render(response, "main/index.html", {})
