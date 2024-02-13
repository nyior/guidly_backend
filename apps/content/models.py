from django.db import models

from apps.users.models import CustomUser

from .mixins import ContentModelMixin


class Category(models.Model):
    slug = models.SlugField(max_length=500)
    name = models.CharField(max_length=500)


class Guide(ContentModelMixin):
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
    content = models.TextField()
    guide = models.ForeignKey(
        Guide,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="blogs",
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="blogs",
    )
    authors = models.ManyToManyField(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="guides",
    )
