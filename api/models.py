from django.db import models

# TODO: Write a check to make sure dependencies are assets


class Asset(models.Model):
    path = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    version = models.IntegerField(default=1)
    asset_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    dependencies = models.JSONField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        existing_assets = Asset.objects.filter(name=self.name).order_by("-version")

        if existing_assets.exists():
            self.version = existing_assets[0].version + 1
        else:
            self.version = 1

        super().save(*args, **kwargs)


class Review(models.Model):
    path = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    version = models.IntegerField(default=1)
    review_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    dependencies = models.JSONField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        existing_reviews = Review.objects.filter(name=self.name).order_by("-version")

        if existing_reviews.exists():
            self.version = existing_reviews[0].version + 1
        else:
            self.version = 1

        super().save(*args, **kwargs)


class Pack(models.Model):
    name = models.CharField(max_length=255)
    version = models.IntegerField(default=1)
    pack_type = models.CharField(max_length=255)
    contents = models.JSONField("Contents", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
