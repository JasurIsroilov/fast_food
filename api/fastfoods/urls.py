from rest_framework.routers import SimpleRouter

from api.fastfoods.views import (
    FastFoodViewSet
)


router = SimpleRouter()
router.register(r"", FastFoodViewSet, basename="fastfoods")

urlpatterns = router.urls
