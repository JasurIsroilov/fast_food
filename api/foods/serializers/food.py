from rest_framework import serializers

from apps.foods.models import Food
from api.foods.serializers.category import CategoryListSerializer


class FoodListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(label="ID", read_only=True)
    name = serializers.CharField(max_length=255, read_only=True)
    price = serializers.FloatField(read_only=True)
    description = serializers.CharField(max_length=1000, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "description",
            "created_at",
            "updated_at",
            "category",
        ]


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "description",
            "created_at",
            "updated_at",
            "category",
        ]


class FoodCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "description",
            "category",
        ]


class FoodUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "description",
            "category",
        ]


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "description",
            "created_at",
            "updated_at",
            "category",
        ]
