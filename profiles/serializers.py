from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    last_episode_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["id", "created_at", "last_episode_viewed", "user"]

    def create(self, validated_data) -> Profile:
        profile = Profile.objects.get_or_create(**validated_data)

        return profile


class EpisodeWatchSerializer(serializers.Serializer):
    episode_id = serializers.IntegerField()

    def create(self, validated_data):
        profile = validated_data["profile"]
        episode = validated_data["episode"]

        profile.animes_viewed.add(episode)

        return profile
