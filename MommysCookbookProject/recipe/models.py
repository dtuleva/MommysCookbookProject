from django.db import models
from django.utils.text import slugify

# todo: Validation on model level to have access to it evereywhere - source Doncho
class Recipe(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )

    ingredients = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )

    instructions = models.TextField(
        max_length=3000,
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.pk}")
        return super().save(*args, **kwargs)






# class Recipe(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     ingredients = models.TextField()
#     instructions = models.TextField()
#     rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
#     is_private = models.BooleanField(default=False)
#     slug = models.SlugField(unique=True, blank=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='recipes/', blank=True, default='path/to/default/image.jpg')
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title
