# Generated by Django 4.2.3 on 2023-07-28 05:28

import django.core.validators
from django.db import migrations, models
import validators.validators


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0003_recipe_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(
                blank=True,
                default="recipe_images/recipe_img_default.jpg",
                null=True,
                upload_to="recipe_images",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png"]
                    ),
                    validators.validators.validate_image_max_size_5_mb,
                ],
            ),
        ),
    ]