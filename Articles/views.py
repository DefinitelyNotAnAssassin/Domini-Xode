from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_page    
from django.db import IntegrityError
from Models.models import Announcements 
from Articles.forms import ArticleForm 
from Articles.models import NewsletterMembers
from markdownx.utils import markdownify 
from LandingPage.views import get_referer 




#@cache_page(60 * 60 *  3)
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
        return render(request, 'Articles/partition/articles.html', context=context)
    else:
        return render(request, 'Articles/articles.html', context=context)

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

    return render(request, 'Articles/view_article.html', context={'article': article})


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
        return render(request, 'Articles/add_article.html', context=items)

    elif request.method == 'POST':
        payload = request.POST
        new_article = Announcements(title=payload['title'], author=request.user, content=payload['content'])
        new_article.save()
        return redirect('articles')
    
    
def subscribe_newsletter(request):
    """
    Renders a page for subscribing to the newsletter.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "subscribe newsletter" page.
    """
    
    if request.method == 'POST':
        data = request.POST
        new_member = NewsletterMembers(email=data['email']) 
        try:
            new_member.save() 
        except IntegrityError as e: 
            messages.warning(request, "You are already subscribed to the newsletter.")
            return redirect('articles') 
        
        messages.success(request, "You have successfully subscribed to the newsletter.")
        
        return redirect('articles')