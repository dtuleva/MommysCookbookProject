# Generated by Django 4.2.3 on 2023-07-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, max_length=300)),
                (
                    "ingredients",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                (
                    "instructions",
                    models.TextField(blank=True, max_length=3000, null=True),
                ),
                ("slug", models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]