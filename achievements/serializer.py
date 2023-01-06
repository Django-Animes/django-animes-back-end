from rest_framework import serializers
from .models import Achievement
from users.models import User

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"
    

    def create(self, validated_data):
        achievement,_ = Achievement.objects.get_or_create(name=validated_data['name'])
        return achievement


class UserAchievementsSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        exclude = ["is_superuser","password","last_login","is_staff","groups","user_permissions"]
    
    achievements  = AchievementSerializer(read_only=True,many=True)
    
    def create(self, validated_data):
        user = validated_data['user']
        achievement = validated_data['achievement']
        user.achievements.add(achievement)
        return user
class AchievementUserSerializer(serializers.Serializer):

    achievement_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        user = validated_data['user']
        achievement = validated_data['achievement']
        user.achievements.add(achievement)
        return user