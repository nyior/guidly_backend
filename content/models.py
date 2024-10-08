from django.db import models

from users.models import CustomUser

from .mixins import ContentModelMixin


class Category(models.Model):
    slug = models.SlugField(max_length=500)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.slug}: {self.name}"


class Guide(ContentModelMixin):
    category = models.ManyToManyField(
        Category,
        blank=True,
        related_name="guides",
    )
    authors = models.ManyToManyField(
        CustomUser,
        blank=True,
        related_name="guides",
    )
    technical_editor = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        related_name="guides_reviewed",
        on_delete=models.SET_NULL,
    )
    copy_editor = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        related_name="guides_edited",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.slug}: {self.title}"


class Blog(ContentModelMixin):
    content = models.TextField()
    guide = models.ForeignKey(
        Guide,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="blogs",
    )
    category = models.ManyToManyField(
        Category,
        blank=True,
        related_name="blogs",
    )
    authors = models.ManyToManyField(
        CustomUser,
        blank=True,
        related_name="blog",
    )
    technical_editor = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        related_name="blogs_reviewed",
        on_delete=models.SET_NULL,
    )
    copy_editor = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        related_name="blogs_edited",
        on_delete=models.SET_NULL,
    )
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ["guide", "order"]

    def __str__(self):
        return f"{self.slug}: {self.order}: {self.title}"
