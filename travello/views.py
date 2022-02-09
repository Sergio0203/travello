
from django.shortcuts import render

from travello.models import Destinations, AllDestinations

# Create your views here.
def index(request):
    
    dests= Destinations.objects.all()
    
    alldests=AllDestinations.objects.all()

    return render(request, 'index.html', {'dests': dests, 'alldests': alldests})

