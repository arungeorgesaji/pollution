# Generated by Django 4.1.3 on 2023-01-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="history",
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
                ("message", models.TextField(max_length=1000)),
                ("anonymous", models.BooleanField(default=False)),
                ("PFI", models.BooleanField(default=False)),
            ],
        ),
    ]