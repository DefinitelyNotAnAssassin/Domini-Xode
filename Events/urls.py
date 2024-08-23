from django.urls import path 
from Events import views 


urlpatterns = [ 
    path('events/', views.events, name = 'events'),
    
]