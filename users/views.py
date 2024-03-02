from rest_framework import viewsets

from guidly_backend.utils import generate_slug
from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        name = self.request.data["first_name"] + self.request.data["last_name"]
        slug = generate_slug(name)
        serializer.save(slug=slug)
