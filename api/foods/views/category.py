from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.core.permissions import DjangoModelPermissions
from apps.foods.models import FoodsCategory
from api.foods.serializers.category import CategoryListSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FoodsCategory.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions,]
    ordering = ("name",)
