# Generated by Django 4.2.16 on 2025-05-22 22:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=cloudinary.models.CloudinaryField(
                default="default_piatzt", max_length=255, verbose_name="image"
            ),
        ),
    ]
