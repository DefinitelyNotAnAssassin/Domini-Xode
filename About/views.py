from django.shortcuts import render
from Models.models import Account 
from UserInterface.views import get_referer


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
    OrgRole = dict(OrgRole)

    items = {
            'members': officers,
            'role': OrgRole,
        }
    if get_referer(request):
        return render(request, 'About/partition/about_us.html', context=items)
    else:
        return render(request, 'About/about_us.html', context=items)

