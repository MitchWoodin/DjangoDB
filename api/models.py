import uuid

from django.db import models


def dependency_check():
    # TODO: write a check to make sure dependencies are assets
    pass


class Asset(models.Model):
    id = models.UUIDField(
        primary_key=True,
        max_length=255,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    path = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    dependencies = models.JSONField(null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.UUIDField(
        primary_key=True, max_length=255, default=uuid.uuid4, unique=True
    )
    path = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    shot = models.CharField(max_length=255)
    dependencies = models.JSONField("Dependencies", null=True)

    def __str__(self):
        return self.name


class Pack(models.Model):
    id = models.UUIDField(
        primary_key=True, max_length=255, default=uuid.uuid4, unique=True
    )
    name = models.CharField(max_length=255)
    pack_type = models.CharField(max_length=255)
    contents = models.JSONField("Contents", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
