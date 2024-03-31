# Generated by Django 5.0.3 on 2024-03-31 04:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_rename_views_blog_views_count_alter_blog_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Дата создания"
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="preview",
            field=models.ImageField(
                blank=True, null=True, upload_to="blog_previews/", verbose_name="Превью"
            ),
        ),
    ]
