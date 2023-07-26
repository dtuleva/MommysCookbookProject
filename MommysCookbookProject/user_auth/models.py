from django.contrib.auth import models as auth_models
from django.db import models


class CookbookUser(auth_models.AbstractUser):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 50
    PROFILE_PICTURE_MAX_SIZE = 1048576 # 1MB

    email = models.EmailField(
        unique=True,
        blank=True,
        null=True,
    )

    screen_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
