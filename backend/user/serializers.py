from .models import UserAccount
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        exclude = ['password', 'user_permissions', 'is_staff', 'is_superuser']
    

class PasswordChangeSerializer(serializers.Serializer):
    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    old_password = serializers.CharField(
        max_length=128,
        error_messages={
            'required': "Old password is required",
            'blank': "Please enter your old password"
        }
    )
    new_password1 = serializers.CharField(
        max_length=128,
        error_messages={
            'required': "New password is required",
            'blank': "Please enter a new password"
        }
    )
    new_password2 = serializers.CharField(
        max_length=128,
        error_messages={
            'required': "Confirm password is required",
            'blank': "Please enter confirm password"
        }
    )

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.user,
            not self.user.check_password(value)
        )
        
        if all(invalid_password_conditions):
            raise serializers.ValidationError("Sorry, Invalid old password")
        return value


    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(user=self.user, data=attrs)

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            update_session_auth_hash(self.request, self.user)

