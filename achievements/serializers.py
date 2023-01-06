from rest_framework import serializers
from .models import Achievement, Achievement_user


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"

    def create(self, validated_data: dict):
        new_Achievement = Achievement.objects.get_or_create(**validated_data)
        return new_Achievement


class AchievementUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement_user
        fields = "__all__"
