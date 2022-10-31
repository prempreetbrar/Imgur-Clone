from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"images", views.ImageViewSet, basename="images")
router.register(r"users", views.UserViewSet, basename="users")
urlpatterns = [path("", include(router.urls))]