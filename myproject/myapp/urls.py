from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/<str:file_name>/', views.success, name='success'),
    path('generate/<str:file_name>/', views.generate, name='generate'),
    
   
   
  
]
