from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.serializers import ValidationError

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend

from api.core.permissions import DjangoModelPermissions
from apps.orders.models import Order
from api.orders.serializers.order import (
    OrderSerializer,
    OrderListSerializer,
    OrderUpdateSerializer,
    OrderCreateSerializer,
    OrderDetailSerializer,
)
from api.orders.serializers.order_item import OrderItemCreateSerializer
from api.orders.utils.delivery import count_delivery_time


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    http_method_names = ['get', 'post', 'put']
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_fields = ['status', 'user']
    ordering_fields = ['created_at', 'delivery_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'create':
            return OrderCreateSerializer
        elif self.action == 'update':
            return OrderUpdateSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='Required all fields',
            properties={
                'latitude': openapi.Schema(type=openapi.TYPE_STRING, description='Latitude float number'),
                'longitude': openapi.Schema(type=openapi.TYPE_STRING, description='Longitude float number'),
                'fastfood': openapi.Schema(type=openapi.TYPE_INTEGER, description='Fast food id'),
                'order_items': openapi.Schema(type=openapi.TYPE_ARRAY,
                                              items=openapi.Schema(
                                                  type=openapi.TYPE_OBJECT,
                                                  description='Order Items',
                                                  properties={
                                                      'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),
                                                      'food': openapi.Schema(type=openapi.TYPE_INTEGER),
                                                  }
                                              ))
            },
        ),
        responses={
            201: openapi.Response(
                description="Order created successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Response message'),
                    }
                )
            )
        }
    )
    def create(self, request, *args, **kwargs):
        order_items = request.data.get("order_items")

        if not order_items:
            return Response({"message": "Order has not items"}, status=status.HTTP_400_BAD_REQUEST)
        for item in order_items:
            if item.get("quantity") == 0:
                return Response({"message": "Food quantity cant be 0"}, status=status.HTTP_400_BAD_REQUEST)

        order_serializer = self.get_serializer_class()(data=request.data)
        try:
            order_serializer.is_valid(raise_exception=True)
        except ValidationError as err:
            return Response({"message": str(err)}, status=status.HTTP_400_BAD_REQUEST)
        new_order = order_serializer.save(user=request.user,
                                          delivery_at=count_delivery_time(data=request.data))

        for item in order_items:
            item["order"] = new_order.id

        order_items_serializer = OrderItemCreateSerializer(data=order_items, many=True)
        try:
            order_items_serializer.is_valid(raise_exception=True)
        except ValidationError as err:
            return Response({"message": str(err)}, status=status.HTTP_400_BAD_REQUEST)

        order_items_serializer.save()

        return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)


class MyOrdersView(generics.GenericAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get',]
    serializer_class = OrderDetailSerializer
    filter_backends = [
        OrderingFilter,
    ]
    ordering_fields = ['created_at', 'delivery_at']

    def get(self, request):
        _queryset = Order.objects.filter(user=request.user.id)
        _serializer = self.serializer_class(_queryset, many=True)
        return Response(_serializer.data)
