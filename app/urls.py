from django.urls import path
from django.contrib import admin
from .views import home,register,login,logout
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',register, name="register"),
    path('register',register, name="register"),
    path('login',login, name="login"),
    path('logout',logout, name="logout"),
    path('home',home,name="home")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)