from django.contrib import admin

from MommysCookbookProject.recipe.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "slug", "title", "description", "ingredients", "instructions")


admin.site.register(Recipe, RecipeAdmin)
