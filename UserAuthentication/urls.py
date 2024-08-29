from django.urls import path 
from LandingPage import views 

urlpatterns = [
      path('login', views.login, name = 'login'),
]