import uuid

from django.db import models


class Asset(models.Model):
    uid = models.UUIDField(max_length=255, default=uuid.uuid4, unique=True)
    path = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    dependencies = models.JSONField("self", null=True)


class Review(models.Model):
    uid = models.UUIDField(max_length=255, default=uuid.uuid4, unique=True)
    path = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    shot = models.CharField(max_length=255)
    dependencies = models.JSONField("self", null=True)


class Pack(models.Model):
    uid = models.UUIDField(max_length=255, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    pack_type = models.CharField(max_length=255)
    contents = models.JSONField("self", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
