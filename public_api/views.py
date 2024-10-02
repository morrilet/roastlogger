from rest_framework.viewsets import ModelViewSet
from public_api.serializers import UserSerializer
from public_api.permissions import UserPermission
from accounts.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermission]