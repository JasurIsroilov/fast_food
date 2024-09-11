from rest_framework import serializers

from apps.orders.models import OrderItem
from api.foods.serializers.food import FoodDetailSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    food = FoodDetailSerializer()

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "quantity",
            "food",
        ]


class OrderItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "quantity",
            "food",
            "order",
        ]
