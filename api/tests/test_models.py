import json

from api.tests.factories import AssetFactory, ReviewFactory, PackFactory
from conftest import aaa_db


class TestAsset:
    def test_factory(self):
        asset = AssetFactory()

        assert asset is not None

        assert asset.id != ""
        assert asset.path != ""
        assert asset.name != ""
        assert asset.asset_type != ""
        assert asset.created_by != ""

        # TODO: Test items not in Factory

    def test_dependencies(self):
        asset = AssetFactory()
        sub_factories = AssetFactory.create_batch(2)
        sub_one_id = sub_factories[0].id
        sub_two_id = sub_factories[1].id
        asset.dependencies = str({"assets": [sub_one_id, sub_two_id]})

        json_convert = asset.dependencies.replace("'", '"')

        json_data = json.loads(json_convert)

        assert str(asset.dependencies) != ""
        assert json_data["assets"][0] == sub_factories[0].id
        assert json_data["assets"][1] == sub_factories[1].id

    def test_string_name(self):
        asset = AssetFactory()

        assert str(asset) == asset.name


class TestReview:
    def test_factory(self):
        review = ReviewFactory()

        assert review is not None

        assert review.id != ""
        assert review.path != ""
        assert review.name != ""
        assert review.asset_type != ""
        assert review.created_by != ""
        assert review.shot != ""

        # TODO: Test items not in Factory

    def test_string_name(self):
        review = ReviewFactory()

        assert str(review) == review.name


class TestPack:
    def test_factory(self):
        pack = PackFactory()

        assert pack is not None

        assert pack.name != ""
        assert pack.pack_type != ""
        assert pack.contents != ""

        # TODO: Test items not in Factory

    def test_string_name(self):
        pack = PackFactory()

        assert str(pack) == pack.name
