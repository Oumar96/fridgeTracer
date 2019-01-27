from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "Tracker/home.html")

def addItem(request):
    return render(request, "Tracker/addItem.html")

def removeItem(request):
    return render(request, "Tracker/removeItem.html")