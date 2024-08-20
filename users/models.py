from django.contrib.auth.models import AbstractUser
from django.db import models


# Authord or Technical Editor or Copy Editor
class ContentCreatorType(models.Model):
    slug = models.SlugField(max_length=500)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.slug}: {self.name}"


class CustomUser(AbstractUser):
    username = models.SlugField(max_length=1000, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True, max_length=1000)
    author_type = models.ForeignKey(
        ContentCreatorType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="authors",
    )

    def __str__(self) -> str:
        return f"{self.first_name}: {self.last_name}"
