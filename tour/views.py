from django.shortcuts import render
from tour.models import Category, Destination

# Create your views here.
def destination(request):
    destionations=Destination.objects.all()
    return render(request,'tour_destination.html',{'destinations':destionations})