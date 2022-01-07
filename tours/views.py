from django.shortcuts import redirect, render
from tours.forms import destForm

from tours.models import Destination

# Create your views here.
def tour_destinations(request):
    destinations=Destination.objects.all()
    return render(request,'destinations.html',{'destinations':destinations})

def a_tour_destination(request,id_val):
    dest=Destination.objects.get(id=id_val)
    return render(request,'dest.html',{'dest':dest})

def tour_destionation_link(request):
    destinations=Destination.objects.all()
    return render(request,'dest_link.html',{'destinations':destinations})


def add_destination(request):
    form=destForm()
    if request.method=='POST':
        form=destForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_destinations')
    return render(request,'add_destination.html',{'form':form})