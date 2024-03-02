# Generated by Django 5.0.1 on 2024-03-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_customuser_bio_customuser_profile_picture_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="slug",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.SlugField(max_length=500, unique=True),
        ),
    ]