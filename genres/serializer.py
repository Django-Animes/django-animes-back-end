from rest_framework import serializers
from .models import Genre
from animes.models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Anime
        exclude = ('amount_of_episodes',"genres")

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
    animes = AnimeSerializer(many=True)

    def create(self, validated_data: dict):
        genre = validated_data["name"]
        genre, _ = Genre.objects.get_or_create(name=genre)
        return genre
