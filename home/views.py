from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse('<b1>Hello World! Welcome to Home</b1> (HttpResponse)')