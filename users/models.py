from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    slug = models.SlugField(max_length=500)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.URLField(max_length=1000)
