from django.urls import path
from api.account.views import (
    UserRegisterAPIView,
    DecoratedTokenRefreshView,
    DecoratedTokenObtainPairView,
)


urlpatterns = [
    path('token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterAPIView.as_view(), name='user_register'),
]
