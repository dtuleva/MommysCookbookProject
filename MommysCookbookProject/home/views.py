from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from MommysCookbookProject.home.forms import NoteForm
from MommysCookbookProject.home.models import Favorite, Note
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
def note_create(request, slug):
    recipe = Recipe.objects.get(slug=slug)

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note_instance = form.save(commit=False)
            new_note_instance.to_recipe = recipe
            new_note_instance.owner = request.user
            new_note_instance.save()

        return redirect(request.META['HTTP_REFERER'] + "#notes")


@login_required
def note_edit(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, owner=request.user)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse("recipe_details", kwargs={"slug": note.to_recipe.slug}) + '#notes')

    form = NoteForm(instance=note)
    return render(request, template_name="home/note_edit.html", context={'note_form': form, 'note': note})


@login_required
def note_delete(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk, owner=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect(reverse("recipe_details", kwargs={"slug": note.to_recipe.slug}) + '#notes')

    return render(request, template_name="home/note_delete.html", context={'note': note})



