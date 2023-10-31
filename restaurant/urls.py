from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('ingredients', views.Ingredients.as_view(), name='inventory'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('menu/<pk>', views.Recipe.as_view(), name='recipe'),
]