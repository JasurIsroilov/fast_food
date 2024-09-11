from rest_framework import serializers

from apps.fastfoods.models import FastFood
from api.foods.serializers.food import FoodSerializer


class FastFoodListSerializer(serializers.ModelSerializer):

    food = FoodSerializer(many=True)

    class Meta:
        model = FastFood
        fields = [
            "id",
            "name",
            "latitude",
            "longitude",
            "food",
        ]


class FastFoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastFood
        fields = [
            "id",
            "name",
            "latitude",
            "longitude",
        ]
