from django.urls import path
from CodeEditor import views 



urlpatterns = [
    path('', views.code_editor, name='code_editor'),
    path('run_code/', views.run_code, name='run_code'),
    
]