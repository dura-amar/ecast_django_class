from django.shortcuts import redirect, render
from tours.forms import destForm, distForm
from django.contrib.auth.decorators import login_required
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

@login_required
def add_destination(request):
    form=destForm()
    if request.method=='POST':
        form=destForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_destinations')
    return render(request,'add_destination.html',{'form':form})


def update_destiantion(request,dId):
    dest=Destination.objects.get(id=dId)
    form=destForm(instance=dest)
    if request.method=='POST':
        form=destForm(request.POST, instance=dest)
        if form.is_valid():
            form.save()
        return redirect('all_destinations')
    return render(request,'updateDest.html',{'form':form}) 

def delete_destination(request,dId):
    obj=Destination.objects.get(id=dId)
    obj.delete()
    return redirect('all_destinations') 

def add_district(request):
    form=distForm()
    if request.method=='POST':
        form=distForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_destinations')
    return render(request,'add_district.html',{'form':form})