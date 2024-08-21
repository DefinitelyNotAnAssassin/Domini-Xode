from django.shortcuts import render
from Models.models import Events
from UserInterface.views import get_referer
# Create your views here.


def events(request):
    
    q = Events.objects.all().order_by('-event_start_date')
    items = {
            'events': q
        }
    if get_referer(request):
        return render(request, 'Events/partition/events.html', context = items)
    else:
        return render(request, 'Events/events.html', context = items)
    
