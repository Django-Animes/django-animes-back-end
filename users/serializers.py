from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "type",
            "is_superuser",
            "is_active",
        ]
        extra_kwargs = {
            id: {"read_only": True},
            "email": {
                "required": True,
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="Username is already in use.",
                    )
                ],
            },
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"]:
            return User.objects.create_superuser(validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
