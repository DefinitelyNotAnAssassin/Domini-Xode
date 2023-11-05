from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from Models.models import * 
from UserInterface.forms import ArticleForm
from markdownx.utils import markdownify
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
import openai
# Credits to stackoverflow for this 404 catcher 
def bad_request(request, exception):
    return redirect('index')

# Credits to stackoverflow for this genius hack 
def get_referer(request):
    is_HTMX = request.META.get('HTTP_HX_REQUEST')
    if not is_HTMX:
        return False 
    
    else:
        return True
def index(request):
    """
    Renders the index page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered index page.
    """
    if get_referer(request):
        return render(request, 'UserInterface/partition/index.html')
    else:
        return render(request, 'UserInterface/index.html')

def articles(request):
    """
    Renders a page displaying a list of articles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered articles page.
    """
    
    
    q = Announcements.objects.all().order_by('-date')
    context = {
            'announcements': q
        }
    if get_referer(request):
        return render(request, 'UserInterface/partition/articles.html', context=context)
    else:
        return render(request, 'UserInterface/articles.html', context=context)

def view_article(request, id):
    """
    Renders a page to view a specific article.

    Args:
        request (HttpRequest): The request object.
        id (int): The ID of the article to view.

    Returns:
        HttpResponse: Rendered article view page.
    """
    article = get_object_or_404(Announcements, id=id)
    article.content = markdownify(article.content)

    return render(request, 'UserInterface/view_article.html', context={'article': article})

def about_us(request):
    """
    Renders a page displaying information about the organization's officers and roles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "about us" page.
    """

    
    officers = Account.objects.filter(role__range=[1, 12])
    OrgRole = [(1, 'President'), (2, 'Internal Vice President'), (3, 'External Vice President'),
                (4, 'Treasurer'), (5, 'Secretary'), (6, "Assistant Secretary"), (7, "Auditor"),
                (8, "Outreach Program Director"), (9, "Event Coordinator"), (10, "Public Information Officer"),
                (11, "Digital Officer"), (12, "Representative"), (13, 'Member')]
    abc = dict(OrgRole)

    items = {
            'members': officers,
            'role': abc,
        }
    if get_referer(request):
        return render(request, 'UserInterface/partition/about_us.html', context=items)
    else:
        return render(request, 'UserInterface/about_us.html', context=items)


def contact_us(request):
    """
    Renders a page for contacting the organization.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "contact us" page or handles form submission.
    """



    if request.method == 'POST':
        data = request.POST
        msg = Messages(email=data['email'], full_name=data['fullname'], msg=data['message'], phone_number=data['phone'])
        msg.save()
        send_mail(subject = f"Domini Xode - Contact Us - {data['fullname']}",  message = f"""
Name: {data['fullname']}
<{data['email']}>
Contact #: {data['phone']}

{data['message']}
        """, from_email = settings.EMAIL_HOST_USER, recipient_list = ['bsit.dominixode@sdca.edu.ph', 'winmari.manzano@sdca.edu.ph'])
        
        messages.success(request, "Message sent. The organization will respond in the email / phone number provided.")
        
        return render(request, 'UserInterface/index.html')
    


    elif request.method == 'GET':
        if get_referer(request):
            
            return render(request, 'UserInterface/partition/contact_us.html')
        else:
            return render(request, 'UserInterface/contact_us.html')

@login_required
def add_article(request):
    """
    Renders a page for adding a new article or handles article submission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "add article" page or redirects after submission.
    """
    if request.method == 'GET':
        form = ArticleForm()
        items = {
            'form': form,
        }
        return render(request, 'UserInterface/add_article.html', context=items)

    elif request.method == 'POST':
        payload = request.POST
        new_article = Announcements(title=payload['title'], author=request.user, content=payload['content'])
        new_article.save()
        return redirect('articles')

def login(request):
    """
    Renders a login page or handles user authentication.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered login page or a success message upon successful login.
    """
    if request.method == 'GET':
        return render(request, 'UserInterface/login.html')
    elif request.method == 'POST':
        isExisting = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if isExisting:
            login_user(request, isExisting)
            return HttpResponse("Login Successfully")
        else:
            redirect('login')
        return HttpResponse("To implement")
    else:
        return HttpResponse("Invalid METHOD")


def events(request):
    
    q = Events.objects.all().order_by('-event_start_date')
    items = {
            'events': q
        }
    if get_referer(request):
        return render(request, 'UserInterface/partition/events.html', context = items)
    else:
        return render(request, 'UserInterface/events.html', context = items)
    

def coding_ai(request):
    
    if get_referer(request):
        return render(request, 'UserInterface/partition/coding_ai.html')
    else:
        return render(request, 'UserInterface/coding_ai.html')


def html_prettier(request):
    if get_referer(request):
        return render(request, 'UserInterface/partition/html_prettier.html')
    else:
        return render(request, 'UserInterface/html_prettier.html')