from rest_framework import viewsets

from content.models import Blog, Category, CustomUser, Guide
from content.serializers import BlogSerializer, CategorySerializer, GuideSerializer
from guidly_backend.utils import generate_slug

# TODO: Refactor repeated code here


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"

    def perform_create(self, serializer):
        name = self.request.data["name"]
        slug = generate_slug(name)
        serializer.save(slug=slug)


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    lookup_field = "slug"

    def perform_create(self, serializer):
        title = self.request.data["title"]
        slug = generate_slug(title)
        guide = serializer.save(slug=slug)

        authors = self.request.data["authors"]
        for author in authors:
            try:
                a = CustomUser.objects.get(slug=author["slug"])
                guide.authors.add(a)
            except Exception:
                raise Exception

        return guide


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"

    def perform_create(self, serializer):
        title = self.request.data["title"]
        slug = generate_slug(title)
        blog = serializer.save(slug=slug)

        authors = self.request.data["authors"]
        for author in authors:
            try:
                a = CustomUser.objects.get(slug=author["slug"])
                blog.authors.add(a)
            except Exception:
                raise Exception

        return blog
