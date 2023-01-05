from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from achievements.serializer import  AchievementSerializer
from achievements.models import Achievement
import ipdb

class UserSerializer(serializers.ModelSerializer):
    # achievements = AchievementSerializer(many=True)
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
            
            for data in achievement_data:
                instance.achievements.add(data)
                
                
                
            
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
    
    

  

""" get_create_achievement = Achievement.objects.get(data)
                 """
                 
                 
"""   def update(self, instance: User, validated_data: dict) -> User:
      
        if validated_data.get("achievements"):
            
            achievement_data = validated_data.pop("achievements")
            
            for data in achievement_data:
                instance.achievements.add(data)
                
                
            
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance """