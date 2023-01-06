from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from achievements.serializer import  AchievementSerializer
from achievements.models import Achievement

import ipdb

class UserAchievementSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Achievement
        fields = [
            "id", 
            "name", 
            "url", 
            "type_of_achievement"
            ]
        read_only_fields = [
            "url",
            "name",
            "type_of_achievement"
        ]
       
        
    

class UserSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True)
    class Meta:
        model = User
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
            "achievements"
        ]
        extra_kwargs = {
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
            "achievements": {"allow_null": True, "required": False},
        }
        
        

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"]:
            super_user = User.objects.create_superuser(**validated_data)
            return super_user
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance: User, validated_data: dict) -> User:
        if validated_data.get("achievements"):
            achievement_data = validated_data.pop("achievements")
            achievement = Achievement.objects.get(id=achievement_data[0]["id"]) 
            
            if achievement:
                instance.achievements.add(achievement)
       
                  
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
    
