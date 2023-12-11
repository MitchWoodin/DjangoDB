import factory


class AssetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "api.Asset"

    uid = factory.Faker("uuid4")
    asset_type = factory.Faker("word")
    created_by = factory.Faker("name")
    path = factory.Faker("file_path")
    name = factory.Faker("file_name")
    dependencies = ""


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "api.Review"

    uid = factory.Faker("uuid4")
    path = factory.Faker("file_path")
    name = factory.Faker("file_name")
    shot = factory.Faker("file_name")
    asset_type = factory.Faker("word")
    created_by = factory.Faker("name")


class PackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "api.Pack"

    name = factory.Faker("file_name")
    pack_type = factory.Faker("word")
    contents = factory.Faker("json")
