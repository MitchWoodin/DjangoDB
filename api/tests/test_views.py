from api.tests.factories import AssetFactory
from rest_framework.test import APIClient

from ..views import AssetViewSet, ReviewViewSet, PackViewSet


class TestAssetView:
    url = "/api/asset/"

    def test_asset_view_response(self):
        response = APIClient().get(self.url)

        assert response.status_code == 200


class TestReviewView:
    url = "/api/review/"

    def test_review_view_response(self):
        response = APIClient().get(self.url)

        assert response.status_code == 200


class TestPackView:
    url = "/api/pack/"

    def test_pack_view_response(self):
        response = APIClient().get(self.url)

        assert response.status_code == 200
