# Generated by Django 4.2.3 on 2023-07-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_auth", "0002_alter_cookbookuser_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="cookbookuser",
            name="profile_picture",
            field=models.TextField(blank=True, null=True),
        ),
    ]
