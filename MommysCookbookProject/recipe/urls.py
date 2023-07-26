from django.urls import path

from MommysCookbookProject.recipe.views import RecipesListView, RecipeDetailsView, RecipeCreateView, RecipeEditView, \
    RecipeDeleteView

urlpatterns = [
    path("", RecipesListView.as_view(), name="recipes_list"),
    path("add", RecipeCreateView.as_view(), name = "recipe_create"),
    path("<str:slug>/", RecipeDetailsView.as_view(), name="recipe_details"),
    path("edit/<str:slug>/", RecipeEditView.as_view(), name="recipe_edit"),
    path("delete/<str:slug>/", RecipeDeleteView.as_view(), name="recipe_delete"),
]