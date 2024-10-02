from rest_framework.serializers import ModelSerializer
from accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        queryset = User.objects.all()
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data['password']
        del validated_data['password']

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        return user