from django.db import models

from apps.users.models import CustomUser


class Category(models.Model):
    slug = models.SlugField(max_length=500)
    name = models.CharField(max_length=500)


class Guide(models.Model):
    slug = models.SlugField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="guides",
    )
    authors = models.ManyToManyField(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="guides",
    )


class Blog(models.Model):
    slug = models.SlugField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="guides",
    )
    authors = models.ManyToManyField(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="guides",
    )


# TODO: blog and guide models look really similar - refactor
