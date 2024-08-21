from django.shortcuts import render, redirect
from django.contrib import messages 
from django.core.mail import send_mail 
from django.conf import settings
from Models.models import Messages
from UserInterface.views import get_referer


# Create your views here.




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
        return redirect('index')
    
    elif request.method == 'GET':
        if get_referer(request):
            return render(request, 'Contact/partition/contact_us.html')
        else:
            return render(request, 'Contact/contact_us.html')
