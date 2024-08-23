from django.urls import path 
from Articles import views 


urlpatterns = [ 
    path('', views.articles, name = 'articles'),
    path('view_article/<int:id>', views.view_article, name = 'view article'),
    path('add_article', views.add_article, name = 'add article'),
               ]