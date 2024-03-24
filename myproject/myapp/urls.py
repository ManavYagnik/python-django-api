from django.urls import path
from . import views
from .views import download_file

urlpatterns = [
    path('', views.home, name='home'),
    path('success/<str:file_name>/', views.success, name='success'),
    path('generate/<str:file_name>/', views.generate, name='generate'),
    path('download_file/', download_file, name='download_file'),
      
]

