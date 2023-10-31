from typing import Any
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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

class UpdateIngredient(LoginRequiredMixin, UpdateView):
   model = Ingredient
   template_name = 'restaurant/form.html'
   form_class = forms.IngredientForm

   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context['form_heading'] = 'Update Ingredient'
      return context
   
class DeleteIngredient(LoginRequiredMixin, DeleteView):
   model = Ingredient
   template_name = 'restaurant/delete_form.html'
   success_url = reverse_lazy('inventory')

class Menu(ListView):
   model = MenuItem
   template_name = 'restaurant/menu.html'

class CreateMenuItem(LoginRequiredMixin, CreateView):
   model = MenuItem
   template_name = 'restaurant/form.html'
   form_class = forms.MenuItemForm

   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context['form_heading'] = 'Add Menu Item'
      return context
   
class CreateMenuIngredient(LoginRequiredMixin, CreateView):
   model = IngredientRequirement
   form_class = forms.IngredientRequirementForm
   template_name = 'restaurant/form.html'

   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context['form_heading'] = f"Add Ingredient to {MenuItem.objects.get(pk=self.kwargs['pk'].title())}"
      return context

   def get_form_kwargs(self) -> dict[str, Any]:
      kwargs = super().get_form_kwargs()
      kwargs['initial']['menu_item'] = MenuItem.objects.get(pk=self.kwargs['pk'])
      return kwargs
   
   def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        success_url = reverse('recipe', kwargs={'pk': pk})

        return success_url

class Recipe(DetailView):
   model = MenuItem
   template_name = 'restaurant/recipe.html'