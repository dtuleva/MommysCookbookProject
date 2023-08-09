from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from MommysCookbookProject.recipe.models import Recipe


class Note(models.Model):
    note_text = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(2),),
        blank=False,
        null=False
    )

    is_private = models.BooleanField(
        blank=False,
        null=False,
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,

    )

    to_recipe = models.ForeignKey(
        to=Recipe,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        ordering = ["-created_at"]


class Favorite(models.Model):
    to_recipe = models.ForeignKey(
        to=Recipe,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
