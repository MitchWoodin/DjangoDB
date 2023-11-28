import uuid

from django.db import models


class Asset(models.Model):
    uid = models.UUIDField(max_length=255, default=uuid.uuid4, unique=True)
    path = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    dependencies = models.JSONField("self", null=True)
    is_review = models.BooleanField(default=False)
