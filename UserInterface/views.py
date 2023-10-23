from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from Models.models import * 
from UserInterface.forms import ArticleForm
from markdownx.utils import markdownify


def index(request):

    print(Account.objects.all().order_by('role'))
    return render(request, 'UserInterface/index.html')

def articles(request):

    q = Announcements.objects.all().order_by('-date')
    context = {
        'announcements' : q
    }
    return render(request, 'UserInterface/articles.html', context = context)

def view_article(request, id):
    article = get_object_or_404(Announcements, id = id)
    article.content = markdownify(article.content)

    return render(request, 'UserInterface/view_article.html', context = {'article': article} )


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


def contact_us(request):
    if request.method == 'POST':
        return HttpResponse("Message sent")
    elif request.method == 'GET':
        return render(request, 'UserInterface/contact_us.html')


def add_article(request):

    if request.method == 'GET':
        form = ArticleForm()
        items = {
            'form': form,

        }
        return render(request, 'UserInterface/add_article.html', context = items)

    elif request.method == 'POST':
        payload = request.POST
        new_article = Announcements(title = payload['title'], author = Account.objects.get(id = 2), content = payload['content'])
        new_article.save()
        return redirect('articles')
