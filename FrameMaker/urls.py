from django.urls import path 
from FrameMaker  import views 


urlpatterns = [
    path('', views.frame_maker, name = 'frame maker'),
]
