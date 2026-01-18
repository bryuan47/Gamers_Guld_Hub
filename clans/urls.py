from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path('clans/', views.clan, name = 'clan_page1'),
    path('admin/', admin.site.urls),
]
