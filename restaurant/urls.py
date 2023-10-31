from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('logout/', views.logout_view, name='logout'),
]