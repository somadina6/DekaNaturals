# Generated by Django 4.2.5 on 2023-11-25 03:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Multivitamins",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=200)),
            ],
        ),
    ]
