from django.urls import path
from .views import IndividRecipeView, MainListView, RecipeAddView, ImageAddView


urlpatterns = [
    path('recipes/list', MainListView.as_view(), name="list"),
    path(
        'recipe/<int:pk>/add_image',
        ImageAddView.as_view(),
        name="image-add"
        ),
    path('recipe/add', RecipeAddView.as_view(), name="recipe-add"),
    path('recipe/<int:pk>', IndividRecipeView.as_view(), name="recipe"),
]


app_name = "ledger"
