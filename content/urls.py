from django.urls import include, path
from rest_framework import routers

from content.views import BlogViewSet, CategoryViewSet, GuideViewSet

router = routers.DefaultRouter()
router.register(r"tags", CategoryViewSet)
router.register(r"guides", GuideViewSet)
router.register(r"blogs", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
