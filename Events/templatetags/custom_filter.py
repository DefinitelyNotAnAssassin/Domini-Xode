from django.template.defaulttags import register
from django.utils import timezone
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter 
def date_status(date):
    if timezone.now() < date.event_start_date:
        return "Upcoming"
    elif timezone.now() < date.event_start_date and timezone.now() > date.event_end_date:
        return "Ongoing"


    else:
        return "Done"
    

    
