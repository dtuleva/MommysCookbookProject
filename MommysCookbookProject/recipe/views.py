from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views, View

from MommysCookbookProject.recipe.forms import RecipeCreateUpdateForm
from MommysCookbookProject.recipe.models import Recipe, Rating


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
    form_class = RecipeCreateUpdateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("recipe_details", kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['files'] = self.request.FILES
        return kwargs


class RecipeEditView(auth_mixins.LoginRequiredMixin, views.UpdateView): # todo: add owns_rec or is admin permission
    model = Recipe
    template_name = "recipe/recipe_edit.html"
    form_class = RecipeCreateUpdateForm

    def get_success_url(self):
        return reverse_lazy("recipe_details", kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['files'] = self.request.FILES
        return kwargs


class RecipeDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView): # todo: add owns_rec or is admin permission
    model = Recipe
    template_name = "recipe/recipes_delete.html"
    success_url = reverse_lazy("index")


class RateRecipeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=kwargs['slug'])
        stars = int(request.POST.get('stars', 0))
        if 1 <= stars <= 5:
            rating, created = Rating.objects.update_or_create(
                recipe=recipe,
                user=request.user,
                defaults={'stars': stars}
            )
        return redirect('recipe_details', slug=recipe.slug)


