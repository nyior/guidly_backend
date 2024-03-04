from rest_framework import serializers

from content.models import Blog, Category, Guide


class CategorySerializer(serializers.ModelSerializer):
    guides = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id", "slug", "guides"]


class GuideSerializer(serializers.ModelSerializer):
    blogs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Guide
        fields = "__all__"
        read_only_fields = ["id", "slug", "created", "updated", "views"]


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ["id", "slug", "created", "updated", "views"]
