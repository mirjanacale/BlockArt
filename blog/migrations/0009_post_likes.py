# Generated by Django 4.2.16 on 2025-03-07 19:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0008_alter_post_featured_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="blog_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
