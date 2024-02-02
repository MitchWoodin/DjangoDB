from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Asset, Review, Pack
from .serializers import (
    AssetSerializer,
    CreateAssetSerializer,
    PackSerializer,
)


class AssetViewSet(viewsets.ViewSet):
    """API endpoint that allows assets to be viewed or edited."""

    queryset = Asset.objects.all()

    def list(self, request):
        serializer = AssetSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateAssetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ReviewViewSet(viewsets.ViewSet):
    """API endpoint that allows reviews to be viewed or edited."""

    queryset = Review.objects.all()

    def list(self, request):
        serializer = ReviewSerializer(self.queryset, many=True)
        return Response(serializer.data)


class PackViewSet(viewsets.ViewSet):
    """API endpoint that allows packs to be viewed or edited."""

    queryset = Pack.objects.all()

    def list(self, request):
        serializer = PackSerializer(self.queryset, many=True)
        return Response(serializer.data)
