from django.shortcuts import render
from airport.models import Airport

# Create your views here.
def all_airport(request):
    airports=Airport.objects.all()
    context={'page_title':'Airports','airports':airports}
    return render(request,'airport.html',context)