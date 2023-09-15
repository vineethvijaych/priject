from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dnldr/', views.dnldr, name='dnldr'),
    path('yt', views.yt, name='yt'),
    path('download/', views.download, name='download'),
   
]
