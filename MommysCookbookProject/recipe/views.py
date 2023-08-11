from datetime import timedelta

from django.db.models import Avg
from django.utils import timezone

from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views import generic as views, View

from MommysCookbookProject.home.forms import NoteForm
from MommysCookbookProject.home.models import Favorite
from MommysCookbookProject.recipe.forms import RecipeCreateUpdateForm
from MommysCookbookProject.recipe.models import Recipe, Rating


class RecipesListView(views.ListView):
    template_name = "recipe/recipes_list.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('search', '')
        search_title = self.request.GET.get('search_title')
        search_ingredients = self.request.GET.get('search_ingredients')
        search_description = self.request.GET.get('search_description')
        search_instructions = self.request.GET.get('search_instructions')

        chapter = self.request.GET.get('chapter', None)
        not_logged_error_message = None

        if chapter == 'recent':
            viewed_recipes_list = self.request.session.get("viewed_recipes_list", [])
            queryset = queryset.filter(pk__in=viewed_recipes_list)
        if chapter == 'best':
            queryset = queryset.annotate(avg_rating=Avg('rating__stars'))\
                .filter(avg_rating__gt=4.5).order_by('-avg_rating')

        if not self.request.user.is_authenticated and chapter in ('favorites', 'own'):
            not_logged_error_message = "Only logged-in users can access Favorites and My Recipes. " \
                                       "Here are our newest recipes instead:"

        else:
            if chapter == 'favorites':
                favorite_recipes = Favorite.objects.filter(owner=self.request.user).values_list('to_recipe', flat=True)
                queryset = queryset.filter(pk__in=favorite_recipes)

            if chapter == 'own':
                queryset = queryset.filter(owner=self.request.user)

        if chapter == 'new' or not_logged_error_message is not None:
            two_days_ago = timezone.now() - timedelta(days=2)
            queryset = queryset.filter(created_at__gte=two_days_ago)

        if not any([search_title, search_ingredients, search_description, search_instructions]):
            search_title = True

        if search_query:
            if search_title:
                queryset = queryset.filter(title__icontains=search_query)
            if search_ingredients:
                queryset = queryset.filter(ingredients__icontains=search_query)
            if search_description:
                queryset = queryset.filter(description__icontains=search_query)
            if search_instructions:
                queryset = queryset.filter(instructions__icontains=search_query)

        self.request.not_logged_error_message = not_logged_error_message

        return queryset


class RecipeDetailsView(views.DetailView):
    model = Recipe
    template_name = "recipe/recipe_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        owner = self.request.user

        context["is_in_favorites"] = False
        context["notes_public"] = recipe.note_set.filter(is_private=False)
        context["notes_private"] = None
        context["note_form"] = NoteForm

        if not self.request.user.is_anonymous:
            context["is_in_favorites"] = recipe.favorite_set.filter(owner=owner).exists()
            context["notes_private"] = recipe.note_set.filter(owner=owner).filter(is_private=True)

        viewed_recipes_list = self.request.session.get("viewed_recipes_list", [])
        if recipe.pk in viewed_recipes_list:
            viewed_recipes_list.remove(recipe.pk)
        viewed_recipes_list.append(recipe.pk)

        self.request.session["viewed_recipes_list"] = viewed_recipes_list[-10:]

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
