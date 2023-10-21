from django.urls import path 
from . import views

urlpatterns = [

    path('', views.index, name = 'index'),
    path('articles', views.articles, name = 'articles'),
    path('events', views.index, name = 'events'),
    path('about_us', views.about_us, name = 'about us'),
    path('contact_us', views.contact_us, name = 'contact us'),
    path('articles/view_article/<int:id>', views.view_article, name = 'view article')

    


]