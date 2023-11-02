from typing import Any
from django.contrib import admin
from .models import Ingredient, IngredientRequirement, MenuItem, Purchase

admin.site.register(Ingredient)
admin.site.register(IngredientRequirement)
admin.site.register(MenuItem)
admin.site.register(Purchase)