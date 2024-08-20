from django.db import models


class ContentModelMixin(models.Model):
    slug = models.SlugField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    header_image = models.URLField(null=True, blank=True, max_length=1000)

    class Meta:
        abstract = True
