from rest_framework import serializers

from apps.users import constants
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'auth_token',)
        read_only_fields = ('auth_token',)

    def validate_email(self, value):
        """
        Check that there is no user registered will this email already.
        """
        try:
            User.objects.get(email__iexact=value)
        except User.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError(
                constants.USER_WITH_EMAIL_EXISTS
                )

        return value

    def validate(self, data):
        """
        Check that password1 and password2 match.
        """
        if not data['password1'] == data['password2']:
            raise serializers.ValidationError(
                constants.PASSWORDS_DO_NOT_MATCH
                )

        return data

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['email'],
            password=validated_data['password1']
            )
