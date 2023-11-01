from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('ingredients', views.Ingredients.as_view(), name='inventory'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('menu/<pk>/detail', views.Recipe.as_view(), name='recipe'),
    path('purchases', views.Transaction.as_view(), name='transaction'),

    path('ingredients/add', views.CreateIngredient.as_view(), name='create_ingredient'),
    path('ingredients/<pk>/update', views.UpdateIngredient.as_view(), name='update_ingredient'),
    path('ingredients/<pk>/delete', views.DeleteIngredient.as_view(), name='delete_ingredient'),

    path('menu/add', views.CreateMenuItem.as_view(), name='create_menu_item'),
    path('menu/<pk>/ingredients/add', views.CreateMenuIngredient.as_view(), name='create_menu_item_ingredient'),
    path('menu/<pk>/ingredients/<fk>/update', views.UpdateMenuIngredient.as_view(), name='update_menu_item_ingredient'),
    path('menu/<pk>/ingredients/<fk>/delete', views.DeleteMenuIngredient.as_view(), name='delete_menu_item_ingredient'),

    path('menu/<pk>/update', views.UpdateMenuItem.as_view(), name='update_menu_item'),
    path('menu/<pk>/delete', views.DeleteMenuItem.as_view(), name='delete_menu_item'),
]