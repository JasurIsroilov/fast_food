from rest_framework import serializers

from apps.foods.models import FoodsCategory


class CategoryListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(label="ID", read_only=True)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = FoodsCategory
        fields = [
            "id",
            "name",
        ]
