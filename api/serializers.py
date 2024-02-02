from rest_framework import serializers
from .models import Asset, Pack


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"


class CreateAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = (
            "path",
            "name",
            "asset_type",
            "created_by",
            "dependencies",
        )


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = "__all__"


class CreatePackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = (
            "name",
            "pack_type",
            "contents",
        )
