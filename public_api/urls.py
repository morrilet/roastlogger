from django.urls import path
from rest_framework.routers import DefaultRouter
from public_api.views import TokenObtainPairView, TokenRefreshView, UserViewSet

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]

router = DefaultRouter()
router.register("user", UserViewSet)
urlpatterns += router.urls