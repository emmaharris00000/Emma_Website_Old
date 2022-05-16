from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

def cv(request):
    return render(request, "cv.html")

def contact(request):
    return render(request, "contact.html")

def art(request):
    return render(request, "art.html")

def art(request):
    return render(request, "art.html")