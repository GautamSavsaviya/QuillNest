# Generated by Django 5.0.1 on 2024-01-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0002_alter_blog_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                default="default-blog.png", upload_to="blogs/images"
            ),
        ),
    ]