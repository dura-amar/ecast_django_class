from django.shortcuts import render

from tours.models import Destination

# Create your views here.
def tour_destinations(request):
    destinations=Destination.objects.all()
    return render(request,'destinations.html',{'destinations':destinations})

def a_tour_destination(request,id_val):
    dest=Destination.objects.get(id=id_val)
    return render(request,'dest.html',{'dest':dest})