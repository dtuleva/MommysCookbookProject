from django.contrib import admin


from MommysCookbookProject.recipe.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "created_at",
        "owner",
        "image",
    )

admin.site.register(Recipe, RecipeAdmin)
