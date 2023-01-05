from rest_framework import serializers
from .models import Episode
from animes.models import Anime
class AnimeNameSerializer(serializers.Serializer):
    name = serializers.CharField()


class AnimeEpisodeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Episode
        exclude = ("anime",)

    def create(self, validated_data):
        episode = Episode.objects.get_or_create(**validated_data)
        return episode
class EpisodeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Episode
        fields = "__all__"
    anime = AnimeNameSerializer()

    def create(self, validated_data):
        episode = Episode.objects.get_or_create(**validated_data)
        return episode