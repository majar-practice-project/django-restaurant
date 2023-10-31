from django import forms
from django.forms import HiddenInput

from .models import Ingredient, MenuItem, IngredientRequirement

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class IngredientRequirementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['menu_item'].initial = self.initial['menu_item']
        self.fields['menu_item'].widget = HiddenInput()

    class Meta:
        model = IngredientRequirement
        fields = '__all__'
