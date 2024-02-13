from django.db import models


class ContentModelMixin(models.Model):
    slug = models.SlugField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
