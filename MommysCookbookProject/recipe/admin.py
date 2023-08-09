from django.contrib import admin

from MommysCookbookProject.recipe.models import Recipe, Rating


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "created_at",
        "owner",
        "image",
    )
    list_filter = ("created_at", "owner")
    search_fields = ("title", "owner__username")


class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe", "stars")
    list_filter = ("user", "recipe")



admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Rating, RatingAdmin)


