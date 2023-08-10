from django.contrib import admin

from MommysCookbookProject.conversion.models import Measurement, Ingredient


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("name", "unit", "conversion_to_grams", "volume_unit", "precision")


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "grams_in_a_cup")
