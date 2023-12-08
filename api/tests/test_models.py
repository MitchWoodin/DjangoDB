from api.tests.factories import AssetFactory, ReviewFactory, PackFactory


class TestAsset:
    def test_factory(self):
        asset = AssetFactory()

        assert asset is not None

        assert asset.path != ""
        assert asset.name != ""
        assert asset.asset_type != ""
        assert asset.created_by != ""

        # TODO: Test items not in Factory


class TestReview:
    def test_factory(self):
        review = ReviewFactory()

        assert review is not None

        assert review.path != ""
        assert review.name != ""
        assert review.asset_type != ""
        assert review.created_by != ""
        assert review.shot != ""

        # TODO: Test items not in Factory


class TestPack:
    def test_factory(self):
        pack = PackFactory()

        assert pack is not None

        assert pack.name != ""
        assert pack.pack_type != ""
        assert pack.contents != ""

        # TODO: Test items not in Factory
