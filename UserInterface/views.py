from django.shortcuts import render, HttpResponse
from Models.models import * 

def index(request):

    print(Account.objects.all().order_by('role'))
    return render(request, 'UserInterface/index.html')



def articles(request):


    q = Announcements.objects.all()

    context = {


        'announcements' : q
    }
    return render(request, 'UserInterface/articles.html', context = context)


def about_us(request):
    officers = Account.objects.filter(role__range = [1, 11])
    
    OrgRole = [(1, 'President'),(2, 'Internal Vice President'), (3, 'External Vice President'),
    (4, 'Treasurer'), (5, 'Secretary'), 
    (6, "Assistant Secretary"), (7, "Auditor"), (8, "Outreach Program Director"), (9, "Event Coordinator"),
    (10, "Public Information Officer"), (11, "Digital Officer"), (12, "Representative"), (13, 'Member')
    
    
    ]


    abc = dict(OrgRole)
    print(abc.get(5))
    
    items = {
        'members': officers, 
        'role' : abc,  
    }
    return render(request, 'UserInterface/about_us.html', context = items)