from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views import generic as views, View

from MommysCookbookProject.home.forms import NoteForm
from MommysCookbookProject.recipe.forms import RecipeCreateUpdateForm
from MommysCookbookProject.recipe.models import Recipe, Rating
from MommysCookbookProject.user_auth.views import CurrentUserMixin


class RecipesListView(views.ListView):
    template_name = "recipe/recipes_list.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        # context['categories'] = Category.objects.all()
        return context


class RecipeDetailsView(views.DetailView):
    model = Recipe
    template_name = "recipe/recipe_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        owner = self.request.user

        is_in_favorites = recipe.favorite_set.filter(owner=owner).exists()
        context["is_in_favorites"] = is_in_favorites

        notes_public = recipe.note_set.filter(is_private=False)
        context["notes_public"] = notes_public

        notes_private = recipe.note_set.filter(owner=owner).filter(is_private=True)
        context["notes_private"] = notes_private

        note_form = NoteForm
        context["note_form"] = note_form

        return context


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


class RecipeEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Recipe
    template_name = "recipe/recipe_edit.html"
    form_class = RecipeCreateUpdateForm

    def get_success_url(self):
        return reverse_lazy("recipe_details", kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['files'] = self.request.FILES
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeCreateUpdateForm(instance=self.object)
        return context


class RecipeDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
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


