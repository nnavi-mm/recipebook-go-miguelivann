from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    inlines = [RecipeIngredientInLine]
    search_fields = ('name', )
    list_display = ('name',)
    list_filter = ('name', )


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine]
    search_fields = ('name', )
    list_display = ('name',)
    list_filter = ('name', )


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('ingredient','recipe',)
    list_display = ('ingredient', 'recipe',)
    list_filter = ('ingredient','recipe',)
    fieldsets = [
        ('Details',{
            'fields':[
                'quantity', ('ingredient', 'recipe'),
            ]
        }),
    ]



admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient,RecipeIngredientAdmin)
