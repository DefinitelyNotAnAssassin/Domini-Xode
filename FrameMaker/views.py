from django.shortcuts import render
from LandingPage.views import get_referer 
# Create your views here.


def frame_maker(request): 
    """
    Renders a page displaying information about the organization's officers and roles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered "about us" page.
    """
    
    if get_referer(request):
        # variable, data_type, if statements, loop
        # OOP 
        
        
        return render(request, 'FrameMaker/partition/frame_maker.html')
    
    else:
        return render(request, 'FrameMaker/frame_maker.html')
