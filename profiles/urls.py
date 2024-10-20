from django.urls import path
from . import views

urlpatterns = [
     path('userinfo/', views.current_user,name='user_info'), 
    path('userinfo/update/', views.update_user,name='update_user'), 
]