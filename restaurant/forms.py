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
        self.fields['ingredient'].choices = [(choice[0], Ingredient.objects.get(pk=int(choice[0].__str__())).get_name_with_unit().capitalize()) for choice in self.fields['ingredient'].choices if choice[0]!='']
        

    class Meta:
        model = IngredientRequirement
        fields = '__all__'

class IngredientRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = IngredientRequirement
        fields = ('quantity', )