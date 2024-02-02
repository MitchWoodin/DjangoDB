from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"asset", views.AssetViewSet, basename="assetAPI")
router.register(r"pack", views.PackViewSet, basename="packAPI")

urlpatterns = router.urls
