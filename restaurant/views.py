from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from .models import Ingredient, IngredientRequirement, MenuItem, Purchase

# Create your views here.
class HomeView(TemplateView):
  template_name = "restaurant/home.html"

class Login(LoginView):
   redirect_authenticated_user = True

   def get_success_url(self):
    if self.request.user.is_authenticated:
        return reverse('index')
    else:
        return reverse('login')

def logout_view(request):
   logout(request)
   return redirect("index")

class Ingredients(ListView):
   model = Ingredient
   template_name = 'restaurant/inventory.html'

class Menu(ListView):
   model = MenuItem
   template_name = 'restaurant/menu.html'