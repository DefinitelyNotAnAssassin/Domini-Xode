from django.shortcuts import render
from django.views.decorators.cache import cache_page
from Models.models import Events
from LandingPage.views import get_referer
# Create your views here.


#@cache_page(60 * 30)
def events(request):
    
    q = Events.objects.all().order_by('-event_start_date')
    items = {
            'events': q
        }
    if get_referer(request):
        return render(request, 'Events/partition/events.html', context = items)
    else:
        return render(request, 'Events/events.html', context = items)
    
