# Generated by Django 4.2.3 on 2023-07-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0004_alter_recipe_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="title",
            field=models.CharField(default="rec", max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
