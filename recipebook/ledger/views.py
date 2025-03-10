from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

# Create your views here.


class IndividRecipeView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'


class MainListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'
