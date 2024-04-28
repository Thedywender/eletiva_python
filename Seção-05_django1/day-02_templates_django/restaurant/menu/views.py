from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Recipe


def index(request):
    context = {"Restaurant": "Thedy's Restaurant", "recipes": Recipe.objects.all()}
    return render(request, "home.html", context)


def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "details.html", {"recipe": recipe})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect("home-page")
