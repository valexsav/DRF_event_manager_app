from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'role',
            'email',
            'is_superuser',
        )


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'username',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    def validate_first_name(self, first_name):
        if not first_name:
            raise serializers.ValidationError(
                _("First name cannot be empty")
            )
        elif first_name.capitalize() != first_name:
            raise serializers.ValidationError(
                _("First name must be capitalized")
            )
        return first_name

    def validate_username(self, username):
        if not username:
            raise serializers.ValidationError(
                _("Username cannot be empty")
            )
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                _("Username already exists")
            )
        return username

    def validate_password(self, password):
        if not password:
            raise serializers.ValidationError(
                _("Password cannot be empty")
            )
        return password


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username:
            raise serializers.ValidationError({"username": "Username cannot be empty"})
        if not password:
            raise serializers.ValidationError({"password": "Password cannot be empty"})

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({"detail": "Invalid username or password"})

        return data
