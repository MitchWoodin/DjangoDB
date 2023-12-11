from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Asset, Review, Pack
from .serializers import (
    AssetSerializer,
    CreateAssetSerializer,
    ReviewSerializer,
    PackSerializer,
)


class AssetView(generics.ListAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class CreateAssetView(APIView):
    def post(self, request):
        serializer = CreateAssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class PackView(generics.ListAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
