from django.db import models
from django.urls import reverse
# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient', args = [self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', args = [self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
            Ingredient, 
            on_delete = models.SET_NULL, 
            null = True,
            related_name = "recipe"
            )

    recipe = models.ForeignKey(
            Recipe, 
            on_delete = models.SET_NULL, 
            null = True,
            related_name = "ingredients"
            )


    class Meta:
        unique_together = ['quantity', 'ingredient','recipe']
        verbose_name = 'ingredient_for_recipe'
        verbose_name_plural = 'ingredients_for_recipe'
