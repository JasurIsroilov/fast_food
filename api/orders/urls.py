from django.urls import path
from rest_framework.routers import SimpleRouter

from api.orders.views import (
    OrderViewSet,
    MyOrdersView,
)

router = SimpleRouter()
router.register(r"", OrderViewSet, basename="orders")

urlpatterns = [
    path("my-orders", MyOrdersView.as_view()),
]

urlpatterns += router.urls
