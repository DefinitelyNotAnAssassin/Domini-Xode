from django.shortcuts import render, HttpResponse 
from django.http import JsonResponse 
from Models.models import Announcements, Events
from markdownx.utils import markdownify


def getArticles(request): 
    announcements = Announcements.objects.all().values()
    data = [] 
    
    
    for announcement in announcements: 


        data.append({ 
            'title': announcement['title'], 
            'description': announcement['description'], 
            'date': announcement['date'], 
            'id': announcement['id'], 
        })
        
    return JsonResponse(data, safe = False) 

def getArticle(request): 
    id = request.GET.get('id') 
    announcement = Announcements.objects.filter(id = id).first()
    print(announcement)
    data = { 
        'title': announcement.title, 
        'description': announcement.description, 
        'content': markdownify(announcement.content),
        'date': announcement.date, 
        'author': announcement.author.first_name + ' ' + announcement.author.last_name, 
    }

    
    return JsonResponse(data, safe = False)


def getEvents(request):
    events = Events.objects.all().values()
    data = []
    
    for event in events:
        data.append({
          
        'title': event['event_name'],
        'description': event['event_description'],
        'image': event['event_flyer'],
        'location': event['event_location'],
        'startDate': event['event_start_date'],
        'endDate': event['event_end_date'],
        })
        
    return JsonResponse(data, safe = False)

