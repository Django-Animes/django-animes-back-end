from rest_framework import serializers
from django.db import models
from .models import Anime
from genres.serializer import GenreSerializer
from episodes.serializer import EpisodeSerializer
import ipdb

class AnimeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Anime
        fields = "__all__"
    genres = GenreSerializer(many=True)
    episodes = EpisodeSerializer(many=True)
    amount_of_episodes = serializers.SerializerMethodField()

    def get_amount_of_episodes(self,obj):
        return len(obj.episodes.all())

    def create(self, validated_data: dict):
        genres: list = validated_data.pop("genres")
        anime,_ = Anime.objects.get_or_create(**validated_data)
        anime.genres.set(genres)
        return anime

        