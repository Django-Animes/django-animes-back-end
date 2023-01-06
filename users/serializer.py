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
    achievements = AchievementSerializer(many=True, read_only=True)
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
            "is_active",
            "achievements"
        ]
        read_only_fields = ["is_superuser"]
        extra_kwargs = {
            "email": {
                "required": True,
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="Email is already in use.",
                    )
                ],
            },
            "password": {"write_only": True},
        }
        
        

    def create(self, validated_data: dict) -> User:
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
    
