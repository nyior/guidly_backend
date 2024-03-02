from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from guidly_backend.utils import generate_slug
from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "username"

    def perform_create(self, serializer):
        name = self.request.data["first_name"] + self.request.data["last_name"]
        username = generate_slug(name)
        serializer.save(username=username)
