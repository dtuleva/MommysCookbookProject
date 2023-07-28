from django.contrib.auth import models as auth_models
from django.db import models
from django.core.validators import FileExtensionValidator

from validators.validators import validate_image_max_size_1_mb


class CookbookUser(auth_models.AbstractUser):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 50
    # PROFILE_PICTURE_MAX_SIZE = 1048576 # 1MB

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
        upload_to=f"profile_images",
        validators=(
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_max_size_1_mb,
        ),
        blank=True,
        null=True,
        default="profile_images/profile_img_default.jpg",
    )

    def __str__(self):
        return self.username
