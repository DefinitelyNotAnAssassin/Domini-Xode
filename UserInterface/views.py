from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from Models.models import * 
from UserInterface.forms import ArticleForm
from markdownx.utils import markdownify
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate

def index(request):
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

    officers = Account.objects.filter(role__range = [1, 12])
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
        data = request.POST 
        msg = Messages(email = data['email'], full_name = data['fullname'], msg = data['message'], phone_number = data['phone'])
        msg.save()
        messages.success(request, "Message sent. The organization will respond in the email / phone number provided.")
        return redirect("index")
    elif request.method == 'GET':
        return render(request, 'UserInterface/contact_us.html')




@login_required 
def add_article(request):

    if request.method == 'GET':
        form = ArticleForm()
        items = {
            'form': form,

        }
        return render(request, 'UserInterface/add_article.html', context = items)

    elif request.method == 'POST':
        payload = request.POST
        new_article = Announcements(title = payload['title'], author = request.user, content = payload['content'])
        new_article.save()
        return redirect('articles')


def login(request):
    if request.method == 'GET':
        return render(request, 'UserInterface/login.html')
    elif request.method == 'POST':
        isExisting = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if isExisting:
            login_user(request, isExisting)
            return HttpResponse("Login Succesfully")
        else: 
            redirect('login')
        return HttpResponse("To implement")
    else:
        return HttpResponse("Invalid METHOD")