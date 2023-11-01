from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy

class Ingredient(models.Model):
    class IngredientUnit(models.TextChoices):
        TEA_SPOON = 'tbsp', gettext_lazy('teaspoon (tbsp)')
        POUND = 'lbs', gettext_lazy('pound (lbs)')
        OUNCE = 'oz', gettext_lazy('ounce (oz)')
        GRAM = 'g', gettext_lazy('gram (g)')
        NA = 'na', gettext_lazy('N/A')

    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    measure_unit = models.CharField(max_length=5, choices=IngredientUnit.choices, default=IngredientUnit.TEA_SPOON)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def get_name_with_unit(self):
        return f'{self.name} - {self.get_measure_unit_display()}'
    
    def get_absolute_url(self):
        return reverse_lazy('inventory')

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('menu')

class IngredientRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} {self.ingredient.measure_unit} of {self.ingredient.name} in {self.menu_item}'

class Purchase(models.Model):
    timestamp = models.DateTimeField()
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.timestamp} - {self.item}'