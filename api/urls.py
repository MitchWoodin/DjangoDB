from django.urls import path
from . import views

urlpatterns = [
    path("asset/", views.AssetView.as_view(), name="apiAsset"),
    path("review/", views.ReviewView.as_view(), name="apiReview"),
    path("pack/", views.PackView.as_view(), name="apiPack"),
]
