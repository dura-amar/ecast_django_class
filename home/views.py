from django.shortcuts import render
from django.http import HttpResponse
from home.models import Introduction
from home.models import Subject

# Create your views here.
def home_view(request):
    intros=Introduction.objects.all()
    subs=Subject.objects.all()
    return render(request, 'home.html',{'intros':intros,'subs':subs})
