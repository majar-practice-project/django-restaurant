from typing import Any
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Ingredient, IngredientRequirement, MenuItem, Purchase
from . import forms

# Create your views here.
class HomeView(TemplateView):
  template_name = "restaurant/home.html"

class Login(LoginView):
   redirect_authenticated_user = True

#    def get_success_url(self):
#     if self.request.user.is_authenticated:
#         return reverse('index')
#     else:
#         return reverse('login')

def logout_view(request):
   logout(request)
   return redirect("index")

class Ingredients(ListView):
   model = Ingredient
   template_name = 'restaurant/inventory.html'

class CreateIngredient(LoginRequiredMixin, CreateView):
   model = Ingredient
   template_name = 'restaurant/form.html'
   form_class = forms.IngredientForm

   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context['form_heading'] = 'Add Ingredient'
      return context


class Menu(ListView):
   model = MenuItem
   template_name = 'restaurant/menu.html'

class Recipe(DetailView):
   model = MenuItem
   template_name = 'restaurant/recipe.html'