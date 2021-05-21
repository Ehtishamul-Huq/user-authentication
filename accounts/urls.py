from .views import register, loginuser, logoutuser
from django.urls import path
from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
]