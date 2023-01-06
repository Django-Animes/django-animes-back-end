from rest_framework import serializers
from .models import Profile
from episodes.models import Episode


class EpisodeViewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    last_episode_viewed = serializers.SerializerMethodField()
    episodes_viewed = EpisodeViewedSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user"]

    def create(self, validated_data) -> Profile:
        profile = Profile.objects.create(**validated_data)

        return profile

    def get_last_episode_viewed(self, validated_data):
        return ""


class EpisodeWatchSerializer(serializers.Serializer):
    episode_id = serializers.IntegerField()

    def create(self, validated_data):
        profile = validated_data["profile"]
        episode = validated_data["episode"]

        profile.episodes_viewed.add(episode)

        return profile
