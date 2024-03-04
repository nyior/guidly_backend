from rest_framework import serializers

from content.models import Blog, Category, Guide


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id", "slug"]


class GuideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = "__all__"
        read_only_fields = ["id", "slug", "created", "updated", "views"]


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"
