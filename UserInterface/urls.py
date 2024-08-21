from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name = 'index'),
    path('tools/coding_ai', views.coding_ai, name = 'coding ai'),
    path('tools/prettier/html', views.html_prettier, name = 'html prettier'),
    path('upload_file', views.upload_file, name = 'upload file')

]