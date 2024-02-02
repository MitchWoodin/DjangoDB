import json

from api.tests.factories import AssetFactory, ReviewFactory, PackFactory
from conftest import aaa_db


class TestAsset:
    def test_factory(self):
        asset = AssetFactory()

        assert asset is not None

        assert asset.path != ""
        assert asset.name != ""
        assert asset.version == 1
        assert asset.asset_type != ""
        assert asset.created_by != ""

        # TODO: Test items not in Factory

    def test_dependencies(self):
        asset = AssetFactory()
        sub_factories = AssetFactory.create_batch(2)
        sub_one_id = sub_factories[0].path
        sub_two_id = sub_factories[1].path
        asset.dependencies = str({"assets": [sub_one_id, sub_two_id]})

        json_convert = asset.dependencies.replace("'", '"')

        json_data = json.loads(json_convert)

        assert str(asset.dependencies) != ""
        assert json_data["assets"][0] == sub_factories[0].path
        assert json_data["assets"][1] == sub_factories[1].path

    def test_versioning(self):
        asset_one = AssetFactory(name="test.usd")
        asset_two = AssetFactory(name="test.usd")
        asset_three = AssetFactory(name="test2.usd")

        assert asset_one.name == asset_two.name
        assert asset_one.name != asset_three.name
        assert asset_one.version == 1
        assert asset_two.version == 2

        assert asset_three.version == 1

    def test_string_name(self):
        asset = AssetFactory()

        assert str(asset) == asset.name


class TestReview:
    def test_factory(self):
        review = ReviewFactory()

        assert review is not None

        assert review.path != ""
        assert review.name != ""
        assert review.version == 1
        assert review.review_type != ""
        assert review.created_by != ""

    def test_string_name(self):
        review = ReviewFactory()

        assert str(review) == review.name

    def test_versioning(self):
        review_one = ReviewFactory(name="test.exr")
        review_two = ReviewFactory(name="test.exr")
        review_three = ReviewFactory(name="test2.exr")

        assert review_one.name == review_two.name
        assert review_one.name != review_three.name
        assert review_one.version == 1
        assert review_two.version == 2

        assert review_three.version == 1


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
