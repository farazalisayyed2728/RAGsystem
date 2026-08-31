from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models import *
from . import views
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def documentation(request):
    return render(request, 'documentation.html')

def contact(request):
    return render(request, 'contact.html')