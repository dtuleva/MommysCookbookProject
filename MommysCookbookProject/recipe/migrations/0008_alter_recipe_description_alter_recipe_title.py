# Generated by Django 4.2.3 on 2023-08-08 04:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0007_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="title",
            field=models.CharField(
                max_length=100,
                unique=True,
                validators=[django.core.validators.MinLengthValidator(5)],
            ),
        ),
    ]
