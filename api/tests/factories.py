import factory


class AssetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "api.Asset"

    uid = factory.Faker("uuid4")
    path = factory.Faker("file_path")
    name = factory.Faker("file_name")
    asset_type = factory.Faker("word")
