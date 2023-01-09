from rest_framework import serializers
from django.db import models
from .models import Anime
from genres.models import Genre
from episodes.models import Episode
from genres.serializer import GenreSerializer
from episodes.serializer import AnimeEpisodeSerializer
import ipdb

class AnimeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Anime
        fields = "__all__"
    genres = GenreSerializer(many=True,read_only=True)
    episodes = AnimeEpisodeSerializer(many=True,read_only=True)
    amount_of_episodes = serializers.SerializerMethodField()

    def get_amount_of_episodes(self,obj):
        return len(obj.episodes.all()) 

class AnimeEpisodeAddSerializer(serializers.Serializer):
    episode_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        episode = validated_data["episode"]
        anime = validated_data["anime"]

        anime.episodes.add(episode)

        return anime

class AnimeEpisodeAddUpdateSerializer(serializers.ModelSerializer):
    episode_id = serializers.IntegerField(write_only=True)
    class Meta():
        model = Episode
        exclude = ["anime"]

class AnimeGenreAddSerializer(serializers.Serializer):
    genre_id = serializers.IntegerField()

    def create(self, validated_data):
        genre = validated_data["genre"]
        anime = validated_data["anime"]

        anime.genres.add(genre)

        return anime
class AnimeGenreAddUpdateSerializer(serializers.ModelSerializer):
    class Meta():
        model = Genre
        fields = "__all__"

