from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Model, Sum, Count
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Ingredient, IngredientRequirement, MenuItem, Purchase
from . import forms

class HomeView(TemplateView):
    template_name = "restaurant/home.html"

    def get_total_cost(self):
        queryset = Purchase.objects.values('item__ingredientrequirement__ingredient__unit_price').annotate(total_quantity=Sum('item__ingredientrequirement__quantity'))
        return sum([query['item__ingredientrequirement__ingredient__unit_price'] * query['total_quantity'] for query in queryset])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['total_revenue'] = Purchase.objects.aggregate(Sum('item__price'))['item__price__sum']
        context['total_cost'] = self.get_total_cost()
        context['net_profits'] = context['total_revenue'] - context['total_cost']
        return context


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
        context['form_heading'] = f"Add Ingredient to {MenuItem.objects.get(pk=self.kwargs['pk']).__str__().title()}"
        return context

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['initial']['menu_item'] = MenuItem.objects.get(
            pk=self.kwargs['pk'])
        return kwargs

    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        success_url = reverse('recipe', kwargs={'pk': pk})

        return success_url


class UpdateMenuIngredient(LoginRequiredMixin, UpdateView):
    model = IngredientRequirement
    form_class = forms.IngredientRequirementUpdateForm
    template_name = 'restaurant/form.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return IngredientRequirement.objects.get(pk=self.kwargs['fk'])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_heading'] = f"Update Ingredient {IngredientRequirement.objects.get(pk=self.kwargs['fk']).ingredient.get_name_with_unit()}"
        return context
    
    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        success_url = reverse('recipe', kwargs={'pk': pk})

        return success_url

class DeleteMenuIngredient(LoginRequiredMixin, DeleteView):
    model = IngredientRequirement
    template_name = 'restaurant/delete_form.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return IngredientRequirement.objects.get(pk=self.kwargs['fk'])
    
    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        success_url = reverse('recipe', kwargs={'pk': pk})

        return success_url

class Recipe(DetailView):
    model = MenuItem
    template_name = 'restaurant/recipe.html'


class UpdateMenuItem(LoginRequiredMixin, UpdateView):
    model = MenuItem
    form_class = forms.MenuItemForm
    template_name = 'restaurant/form.html'
    success_url = reverse_lazy('menu')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_heading'] = 'Update Menu Item'
        return context


class DeleteMenuItem(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'restaurant/delete_form.html'
    success_url = reverse_lazy('menu')


class Transaction(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'restaurant/transaction.html'


class CreatePurchase(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = forms.PurchaseForm
    template_name = 'restaurant/form.html'
    success_url = reverse_lazy('transaction')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_heading'] = 'Add new Purchase'
        return context


class UpdatePurchase(LoginRequiredMixin, UpdateView):
    model = Purchase
    form_class = forms.PurchaseForm
    template_name = 'restaurant/form.html'
    success_url = reverse_lazy('transaction')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_heading'] = 'Update Purchase'
        return context
    

class DeletePurchase(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = 'restaurant/delete_form.html'
    success_url = reverse_lazy('transaction')