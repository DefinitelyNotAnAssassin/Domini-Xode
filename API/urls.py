from django.urls import path 
from API import views 


urlpatterns = [
    path('codeit', views.codeit, name = 'code it')
]