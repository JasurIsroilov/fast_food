from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from api.core.permissions import DjangoModelPermissions
from api.foods.serializers.food import (
    FoodSerializer,
    FoodListSerializer,
    FoodDetailSerializer,
    FoodCreateSerializer,
    FoodUpdateSerializer,
)
from apps.foods.models import Food


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions,]
    http_method_names = ['get', 'post', 'put', 'delete']

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter
    ]
    filterset_fields = ['name', 'category', 'price']
    ordering = ('name', 'price', 'created_at',)

    def get_serializer_class(self):
        if self.action == 'list':
            return FoodListSerializer
        elif self.action == 'create':
            return FoodCreateSerializer
        elif self.action in ['update', 'partial_update', 'check_dates']:
            return FoodUpdateSerializer
        elif self.action == 'retrieve':
            return FoodDetailSerializer
        return FoodSerializer

    def create(self, request, *args, **kwargs):
        _serializer = self.get_serializer_class()(data=request.data)
        _serializer.is_valid(raise_exception=True)
        _serializer.save(user=request.user)
        return Response(_serializer.data)
