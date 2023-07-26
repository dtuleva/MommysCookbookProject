from django.contrib.auth import mixins as auth_mixins
from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from MommysCookbookProject.recipe.models import Recipe


# maybe todo: success the s out of all models and add mixins for pretty forms and disabled fields(for user too)
class RecipesListView(views.ListView):
    template_name = "recipe/recipes_list.html"
    model = Recipe
    context_object_name = "recipes"


class RecipeDetailsView(views.DetailView):
    model = Recipe
    template_name = "recipe/recipe_details.html"


class RecipeCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Recipe
    template_name = "recipe/recipe_create.html"
    fields = ("title", "description", "ingredients", "instructions")

    def get_success_url(self):
        return reverse_lazy("recipe_details", kwargs={'slug': self.object.slug})


class RecipeEditView(views.UpdateView): # todo: add owns_rec or is admin permission
    model = Recipe
    template_name = "recipe/recipe_edit.html"
    fields = ("title", "description", "ingredients", "instructions")

    def get_success_url(self):
        return reverse_lazy("recipe_details", kwargs={'slug': self.object.slug})


class RecipeDeleteView(views.DeleteView): # todo: add owns_rec or is admin permission
    model = Recipe
    template_name = "recipe/recipes_delete.html"
    success_url = reverse_lazy("index")
    # todo: add are you sure to delete that? page (or popup)
