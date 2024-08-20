from rest_framework import serializers

from users.models import ContentCreatorType, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    creator_type = serializers.SlugRelatedField(
        queryset=ContentCreatorType.objects.all(), slug_field="name"
    )

    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "bio", "profile_picture"]
        read_only_fields = ["id", "username"]
