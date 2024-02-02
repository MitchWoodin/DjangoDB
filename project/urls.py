from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"asset-set", views.AssetViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
