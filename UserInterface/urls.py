from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name = 'index'),
    path('articles', views.articles, name = 'articles'),
    path('events', views.events, name = 'events'),
    path('about_us', views.about_us, name = 'about us'),
    path('contact_us', views.contact_us, name = 'contact us'),
    path('articles/view_article/<int:id>', views.view_article, name = 'view article'),
    path('markdownx/', include('markdownx.urls')),
    path('add_article', views.add_article, name = 'add article'),
    path('login', views.login, name = 'login'),
    path('tools/coding_ai', views.coding_ai, name = 'coding ai'),
    path('tools/prettier/html', views.html_prettier, name = 'html prettier')

    


]