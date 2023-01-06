from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    last_episode_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["id", "created_at", "last_episode_viewed", "user"]
