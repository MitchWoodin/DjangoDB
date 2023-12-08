from api.tests.factories import AssetFactory


class TestAsset:
    def test_factory(self):
        asset = AssetFactory()

        assert asset is not None

        assert asset.uid != ""
        assert asset.path != ""
        assert asset.name != ""
        assert asset.asset_type != ""
