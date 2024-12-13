from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

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
            'username',
            'password',
            'first_name',
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
        )
        return user

    def validate_first_name(self, value):
        if value.capitalize() != value:
            raise serializers.ValidationError("First name must be capitalized")
        return value
