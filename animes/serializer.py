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
        
    def create(self, validated_data: dict):
        anime,_ = Anime.objects.get_or_create(**validated_data)
        return anime
    def update(self, instance : dict, validated_data: dict):
        episodes = validated_data.pop("episodes",None)
        genres = validated_data.pop("genres",None)
        for key,value in validated_data.items():
            setattr(instance,key,value)
        return instance       

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