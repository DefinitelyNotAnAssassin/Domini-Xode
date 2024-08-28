from django.shortcuts import render
from About.models import Year, Officer
from LandingPage.views import get_referer


def about_us(request):
    """
    Renders a page displaying information about the organization's officers and roles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "about us" page.
    """

 
    if get_referer(request):
        return render(request, 'About/partition/about_us.html')
    else:
        return render(request, 'About/about_us.html')

def yearlist(request): 
    years = Year.objects.all() 
    items = {'years': years} 
    
    if get_referer(request):
        return render(request, 'About/partition/yearlist.html', context = items)
    else:  
        return render(request, 'About/yearlist.html', context = items)



def mission(request):
    """
    Renders a page displaying the organization's mission statement.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "mission" page.
    """
    if get_referer(request):
        return render(request, 'About/partition/mission.html')
    else:
        return render(request, 'About/mission.html')

def testimonials(request):
    """
    Renders a page displaying testimonials from organization members.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "testimonials" page.
    """
    if get_referer(request):
        return render(request, 'About/partition/testimonials.html')
    else:
        return render(request, 'About/testimonials.html')