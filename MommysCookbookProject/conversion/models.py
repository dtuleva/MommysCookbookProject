from django.core.validators import MinValueValidator
from django.db import models


class Measurement(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    conversion_to_grams = models.FloatField(
        validators=(MinValueValidator(0.0),),
    )
    volume_unit = models.BooleanField(default=False)

    precision = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.unit} ({self.name})"


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    grams_in_a_cup = models.PositiveIntegerField()

    def __str__(self):
        return self.name

