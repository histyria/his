from django.urls import path
from . import views
app_name = 'HOME'
urlpatterns = [
    path('patiant_file/', views.index, name="index"),
    path('post_patiant/', views.Create_PatiantFile, name="post_patiant"),
    path('', views.index, name='patiant_file'),
    path('validate_saudi_id/', views.validate_saudi_id, name='validate_saudi_id'),
   
    
]