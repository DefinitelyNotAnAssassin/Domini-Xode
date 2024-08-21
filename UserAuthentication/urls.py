from django.urls import path 
from UserAuthentication import views 

urlpatterns = [
      path('login', views.login, name = 'login'),
]