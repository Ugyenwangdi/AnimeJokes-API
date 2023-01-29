# Generated by Django 4.1.5 on 2023-01-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Submission",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("joke", models.TextField(blank=True, null=True)),
                ("anime", models.CharField(max_length=200)),
                ("added", models.DateTimeField(auto_now_add=True)),
                (
                    "_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
            ],
        ),
    ]