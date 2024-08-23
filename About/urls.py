from django.urls import path 
from About import views

urlpatterns = [
    path('about_us', views.about_us, name = 'about us'),
    path('yearlist', views.yearlist, name = 'yearlist'),
    path('mission', views.mission, name = 'mission'),
    path('testimonials', views.testimonials, name = 'testimonials'),
]
