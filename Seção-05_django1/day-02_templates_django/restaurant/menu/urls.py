from django.urls import path
from menu.views import delete_recipe, index, recipe_details

urlpatterns = [
    path("", index, name="home-page"),
    path("recipes/<int:recipe_id>/", recipe_details, name="recipe-details"),
    path("recipes/delete/<int:recipe_id>/", delete_recipe, name="delete_recipe"),
]
