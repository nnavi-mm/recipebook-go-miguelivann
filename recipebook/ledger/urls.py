from django.urls import path
from .views import IndividRecipeView, MainListView


urlpatterns = [
    path('recipes/list', MainListView.as_view(), name="list"),
    path('recipe/<int:pk>', IndividRecipeView.as_view(), name="recipe"),
]


app_name = "ledger"
