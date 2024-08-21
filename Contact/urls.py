from django.urls import path 
from Contact import views 

urlpatterns = [
    path('contact_us', views.contact_us, name='contact'),
]
