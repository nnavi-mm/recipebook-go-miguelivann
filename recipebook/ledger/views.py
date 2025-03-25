from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm

# Create your views here.


class IndividRecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = '/accounts/login'


class MainListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'


class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_add.html'
    redirect_field_name = '/accounts/login'


class ImageAddView(CreateView):
    model = Recipe
    form_class = RecipeImageForm
    template_name = 'ledger/image_add.html'

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={'pk': self.kwargs['pk']})
