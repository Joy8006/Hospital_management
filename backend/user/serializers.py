from .models import UserAccount
from rest_framework import serializers
from django.contrib.auth import get_user_model


UserModel: UserAccount = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        exclude = ['password', 'user_permissions', 'is_staff', 'is_superuser']
    
