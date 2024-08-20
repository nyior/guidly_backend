from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
            "creator_type",
        ]
        read_only_fields = ["id", "username"]
