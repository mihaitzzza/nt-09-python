from rest_framework import serializers
from products.models import Store, Product, Category


class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)

    def __init__(self, *args, user=None, **kwargs):
        self._user = user
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        Store.objects.create(
            owner=self._user,
            name=validated_data['name'],
        )

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []
        # depth = 2

    category = CategorySerializer(many=False)
