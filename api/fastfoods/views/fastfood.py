from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from api.core.permissions import DjangoModelPermissions
from apps.fastfoods.models import FastFood
from api.fastfoods.serializers.fastfood import FastFoodListSerializer


class FastFoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodListSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = ['name']
