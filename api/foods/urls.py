from rest_framework.routers import SimpleRouter

from api.foods.views import (
    CategoryViewSet,
    FoodViewSet,
)


router = SimpleRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"", FoodViewSet, basename="foods")

urlpatterns = router.urls
