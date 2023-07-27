from django.db import models
from django.utils.text import slugify

from MommysCookbookProject.user_auth.models import CookbookUser


# todo: Validation on model level to have access to it evereywhere - source Doncho
class Recipe(models.Model):
    TITLE_MAX_LEN = 50
    DESCRIPTION_MAX_LEN = 300
    INGREDIENTS_MAX_LEN = 1000
    INSTRUCTIONS_MAX_LEN = 5000

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        blank=True,
        null=True,
    )

    ingredients = models.TextField(
        max_length=INGREDIENTS_MAX_LEN,
        blank=True,
        null=True,
    )

    instructions = models.TextField(
        max_length=INSTRUCTIONS_MAX_LEN,
        blank=True,
        null=True,
    )

    prep_time = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    cook_time = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    servings = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    owner = models.ForeignKey(
        CookbookUser,
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=None
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

#     rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
#     is_private = models.BooleanField(default=False)
#     slug = models.SlugField(unique=True, blank=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='recipes/', blank=True, default='path/to/default/image.jpg')
