from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from MommysCookbookProject.home.forms import NoteForm
from MommysCookbookProject.home.models import Favorite
from MommysCookbookProject.recipe.models import Recipe


def index(request):
    return render(request, template_name="home/index.html")


@login_required
def favorite_functionality(request, slug):
    recipe = Recipe.objects.get(slug=slug)

    kwargs = {
        'to_recipe': recipe,
        'owner': request.user
    }

    favorite_object = Favorite.objects \
        .filter(**kwargs) \
        .first()

    if favorite_object:
        favorite_object.delete()
    else:
        new_favorite_object = Favorite(**kwargs)
        new_favorite_object.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{slug}")


@login_required
def note_functionality(request, slug):
    recipe = Recipe.objects.get(slug=slug)

    kwargs = {
        'to_recipe': recipe,
        'owner': request.user
    }

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note_instance = form.save(commit=False)
            new_note_instance.to_recipe = recipe
            new_note_instance.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{slug}")
