from rest_framework import serializers
from .models import Episode
from animes.models import Anime
from genres.serializer import GenreSerializer


class AnimeNameSerializer(serializers.Serializer):
    name = serializers.CharField()


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ["id", "name", "image_url", "release_date", "description", "genres"]
        extra_kwargs = {"episodes": {"write_only": True}}

    genres = GenreSerializer(many=True,write_only=True)


class AnimeEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        exclude = ("anime",)

    def create(self, validated_data):
        episode,_ = Episode.objects.get_or_create(**validated_data)
        return episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"

    anime = AnimeSerializer(read_only=True)

    def create(self, validated_data: dict):
        episode,_ = Episode.objects.get_or_create(**validated_data)
        return episode
