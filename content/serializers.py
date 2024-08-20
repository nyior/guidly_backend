from rest_framework import serializers

from content.models import Blog, Category, Guide
from users.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    guides = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id", "slug", "guides"]


class GuideSerializer(serializers.ModelSerializer):
    blogs = serializers.SlugRelatedField(
        many=True, queryset=Blog.objects.all(), slug_field="title"
    )
    authors = serializers.SlugRelatedField(
        many=True, queryset=CustomUser.objects.all(), slug_field="username"
    )
    category = serializers.SlugRelatedField(
        many=True, queryset=Category.objects.all(), slug_field="name"
    )
    technical_editor = serializers.StringRelatedField()
    copy_editor = serializers.StringRelatedField()

    class Meta:
        model = Guide
        fields = "__all__"
        read_only_fields = [
            "id",
            "slug",
            "last_updated",
            "views",
            "blogs",
        ]


class BlogSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        many=True, queryset=CustomUser.objects.all(), slug_field="username"
    )
    category = serializers.SlugRelatedField(
        many=True, queryset=Category.objects.all(), slug_field="name"
    )
    technical_editor = serializers.StringRelatedField()
    copy_editor = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ["id", "slug", "last_updated", "views"]
