from django.shortcuts import render
from rest_framework import generics

from .serializers import AssetSerializer
from .models import Asset


class AssetView(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
