from django.urls import path
from . import views

urlpatterns = [
    path("", views.AssetView.as_view(), name="main"),
]
