from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"images", views.ImageViewSet, basename="images")
images_urlpatterns = [path("", include(router.urls))]