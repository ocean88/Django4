# Generated by Django 5.0.3 on 2024-04-14 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_alter_version_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="Актуальная версия"),
        ),
    ]