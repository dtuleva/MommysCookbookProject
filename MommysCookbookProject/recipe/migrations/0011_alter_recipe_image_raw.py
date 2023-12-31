# Generated by Django 4.2.3 on 2023-08-11 14:11

import django.core.validators
from django.db import migrations, models
import validators.validators


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0010_recipe_image_raw"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image_raw",
            field=models.ImageField(
                blank=True,
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
