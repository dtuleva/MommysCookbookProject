from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify

from validators.validators import validate_image_max_size_5_mb


class Recipe(models.Model):
    TITLE_MAX_LEN = 100
    TITLE_MIN_LEN = 5
    DESCRIPTION_MAX_LEN = 500
    INGREDIENTS_MAX_LEN = 1000
    INSTRUCTIONS_MAX_LEN = 5000

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=(MinLengthValidator(TITLE_MIN_LEN),),
        unique=True,
        blank=False,
        null=False,
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
        auto_now_add=True,
        editable=False,

    )
    owner = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
    image = models.ImageField(
        upload_to="recipe_images",
        validators=(
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_max_size_5_mb,
        ),
        blank=True,
        null=True,
        default="recipe_images/recipe_img_default.jpg",
    )

    def get_average_rating(self):
        ratings = Rating.objects.filter(recipe=self)
        if ratings.exists():
            total_stars = sum(rating.stars for rating in ratings)
            return total_stars / ratings.count()
        return 0

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.pk}")

        return super().save(*args, **kwargs)




#     is_private = models.BooleanField(default=False)



class Rating(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        to=Recipe,
        on_delete=models.CASCADE,
    )
    stars = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    class Meta:
        unique_together = ('user', 'recipe')
