from django.db import models
from django.utils.translation import gettext_lazy

class Ingredient(models.Model):
    class IngredientUnit(models.TextChoices):
        TEA_SPOON = 'tbsp', gettext_lazy('teaspoon (tbsp)')
        POUND = 'lbs', gettext_lazy('pound (lbs)')

    name = models.CharField(max_length=30)
    measure_unit = models.CharField(max_length=5, choices=IngredientUnit.choices, default=IngredientUnit.TEA_SPOON)
    unit_price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class IngredientRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    timestamp = models.DateTimeField()
    items = models.ManyToManyField(MenuItem)