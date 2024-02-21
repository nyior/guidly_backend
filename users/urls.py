from django.urls import include, path
from rest_framework import routers

from users.views import CustomUserViewSet

router = routers.DefaultRouter()
router.register(r"users", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
