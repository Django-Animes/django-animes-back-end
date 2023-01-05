from rest_framework import serializers
from .models import Episode

from animes.models import Anime
from genres.models import Genre
from genres.serializer import GenreSerializer
import ipdb


class AnimeNameSerializer(serializers.Serializer):
    name = serializers.CharField()


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ["id", "name", "image_url", "release_date", "description", "genres"]
        extra_kwargs = {"episodes": {"write_only": True}}

    genres = GenreSerializer(many=True, required=True)


class AnimeEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        exclude = ("anime",)

    def create(self, validated_data):
        episode = Episode.objects.get_or_create(**validated_data)
        return episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"

    anime = AnimeSerializer()

    def create(self, validated_data: dict):
        anime = validated_data.pop("anime", None)
        anime = dict(anime)
        genres = anime.pop("genres", None)
        new_genres = []
        for genre in genres:
            genre = dict(genre)
            genre, _ = Genre.objects.get_or_create(**genre)
            new_genres.append(genre)
        anime, _ = Anime.objects.get_or_create(**anime)
        anime.genres.set(new_genres)
        validated_data["anime"] = anime
        episode, _ = Episode.objects.get_or_create(**validated_data)
        return episode

    def update(self, instance, validated_data: dict):
        anime = validated_data.pop("anime", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance
