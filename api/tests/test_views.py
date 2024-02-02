import factory

from api.tests.factories import AssetFactory
from django.contrib.admin.options import json
from django.urls import reverse
from rest_framework.test import APIClient

from ..views import AssetViewSet, PackViewSet
from ..models import Asset


class TestAssetViewset:
    def test_asset_view_list(self, rf):
        url = reverse("assetAPI-list")
        request = rf.get(url)

        assets = AssetFactory.create_batch(10)

        view = AssetViewSet.as_view({"get": "list"})
        response = view(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 10
        assert json.loads(response.content)[0]["name"] == assets[0].name

    def test_asset_view_create(self, mocker, rf):
        valid_data = factory.build(
            dict,
            FACTORY_CLASS=AssetFactory,
        )
        url = reverse("assetAPI-list")
        request = rf.post(
            url,
            content_type="application/json",
            data=json.dumps(valid_data),
        )

        mocker.patch.object(
            Asset,
            "save",
        )

        view = AssetViewSet.as_view({"post": "create"})

        response = view(request).render()

        assert response.status_code == 200  # TODO: Check status code is 201
        assert json.loads(response.content) == valid_data


class TestPackView:
    url = "/api/pack/"

    def test_pack_view_response(self):
        response = APIClient().get(self.url)

        assert response.status_code == 200
