from rest_framework import serializers

from content.models import Blog, Category, Guide


class CategorySerializer(serializers.ModelSerializer):
    guides = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id", "slug", "guides"]


class GuideSerializer(serializers.ModelSerializer):
    blogs = serializers.StringRelatedField(many=True, read_only=True)
    # TODO: Fix NotImplementedError: StringRelatedField.to_internal_value() must be implemented for field
    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Guide
        fields = "__all__"
        read_only_fields = [
            "id",
            "slug",
            "created",
            "updated",
            "views",
            "blogs",
        ]


class BlogSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ["id", "slug", "created", "updated", "views"]
