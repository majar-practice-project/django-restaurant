from django import forms
from django.forms import inlineformset_factory

from .models import Ingredient, MenuItem, IngredientRequirement

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
