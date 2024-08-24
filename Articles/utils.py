from django.conf import settings 
from django.core.mail import send_mail 
from Articles.models import NewsletterMembers    


def send_newsletter(announcement): 
    """
    Sends a newsletter to all subscribers.

    Args:
        announcement (Announcements): The announcement to send.
    """
    
    EMAIL_LAYOUT = f"""

Domini Xode has posted a new announcement. 
Read it here: https://dominixode.com/articles/view_article/{announcement.id} 

"""

    subscribers = NewsletterMembers.objects.all() 
    
    print("Sending email to subscribers...")
    send_mail(subject = f"Domini Xode - Newsletter [{announcement.title}]", message = EMAIL_LAYOUT, from_email = settings.EMAIL_HOST_USER, recipient_list = [subscriber.email for subscriber in subscribers])

