from django.urls import path 
from API import views 


urlpatterns = [
    path('getArticles', views.getArticles), 
    path('getArticle', views.getArticle),
    path('getEvents', views.getEvents), 
    
]