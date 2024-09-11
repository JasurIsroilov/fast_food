from rest_framework import serializers

from drf_yasg.utils import swagger_serializer_method

from apps.orders.models import Order, OrderItem
from api.fastfoods.serializers.fastfood import FastFoodDetailSerializer
from api.orders.serializers.order_item import OrderItemSerializer, OrderItemCreateSerializer


class OrderListSerializer(serializers.ModelSerializer):

    fastfood = FastFoodDetailSerializer()
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "latitude",
            "longitude",
            "user",
            "fastfood",
            "order_items",
        ]

    @swagger_serializer_method(serializer_or_field=OrderItemSerializer(many=True))
    def get_order_items(self, obj) -> list[OrderItemSerializer] | None:
        queryset = OrderItem.objects.filter(order=obj.id)
        if not queryset:
            return None
        _serializer = OrderItemSerializer(queryset, many=True)
        return _serializer.data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "latitude",
            "longitude",
            "created_at",
            "delivery_at",
            "user",
            "fastfood",
        ]


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["status"]


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            "latitude",
            "longitude",
            "fastfood",
        ]


class OrderDetailSerializer(serializers.ModelSerializer):

    fastfood = FastFoodDetailSerializer()
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "latitude",
            "longitude",
            "created_at",
            "delivery_at",
            "user",
            "fastfood",
            "order_items",
        ]

    @swagger_serializer_method(serializer_or_field=OrderItemSerializer(many=True))
    def get_order_items(self, obj) -> list[OrderItemSerializer] | None:
        queryset = OrderItem.objects.filter(order=obj.id)
        if not queryset:
            return None
        _serializer = OrderItemSerializer(queryset, many=True)
        return _serializer.data
