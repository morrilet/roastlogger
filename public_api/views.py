from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView
from public_api.serializers import UserSerializer
from public_api.permissions import UserPermission
from accounts.models import User
from django.conf import settings


# Custom JWT access handling with HTTP-Only cookie
class TokenObtainPairView(BaseTokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        response.set_cookie(settings.JWT_COOKIE_NAME, token, httponly=True)
        return response


# Custom JWT refresh handling with HTTP-Only cookie
class TokenRefreshView(BaseTokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        response.set_cookie(settings.JWT_COOKIE_NAME, token, httponly=True)
        return response


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermission]