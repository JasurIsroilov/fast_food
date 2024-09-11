from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.core.permissions import (
    DjangoModelPermissions,
    IsWaiterOrAdminModelPermission,
)
from apps.orders.models import OrderItem
from api.orders.serializers.order_item import (
    OrderItemSerializer,
    OrderItemCreateSerializer
)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions,]
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderItemCreateSerializer
        return OrderItemSerializer

    @swagger_auto_schema(
        operation_description="Create several order-items",
        request_body=OrderItemCreateSerializer(many=True),
    )
    def create(self, request, *args, **kwargs):
        for data in request.data:
            _serializer = self.get_serializer_class()(data=data)
            _serializer.is_valid(raise_exception=True)
            self.perform_create(_serializer)
        return Response({"message": "Order items created successfully!"},
                        status=status.HTTP_201_CREATED)


class OrderItemFilterByOrderIdView(generics.GenericAPIView):
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated, IsWaiterOrAdminModelPermission]
    http_method_names = ['get',]
    serializer_class = OrderItemSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('order_id', openapi.IN_QUERY, description="Order Id", type=openapi.TYPE_INTEGER),
    ])
    def get(self, request):
        order_id = request.query_params.get("order_id")
        if not order_id:
            return Response(
                data={"Message": "Order_id does not exist!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        _queryset = OrderItem.objects.filter(order=order_id)
        _serializer = self.serializer_class(_queryset, many=True)
        return Response(_serializer.data)
