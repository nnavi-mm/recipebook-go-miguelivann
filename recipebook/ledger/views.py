from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeForm

# Create your views here.


class IndividRecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = '/accounts/login'


class MainListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'


class RecipeAddView(LoginRequiredMixin,CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/list.html'
    redirect_field_name = '/accounts/login'
