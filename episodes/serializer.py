from rest_framework import serializers
from .models import Episode
from animes.models import Anime
class AnimeNameSerializer(serializers.Serializer):
    name = serializers.CharField()

class AnimeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Anime
        fields = ["id","name","image_url","release_date","description"]
        extra_kwargs = {"episodes" : {"write_only" : True},"genres" : {"write_only" : True}}

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
    anime = AnimeSerializer()

    def create(self, validated_data):
        episode = Episode.objects.get_or_create(**validated_data)
        return episode

    def update(self, instance, validated_data : dict):
        anime = validated_data.pop("anime",None)
        if anime:
            anime,_ = Anime.objects.get_or_create(**anime)
        for key,value in validated_data.items():
            setattr(instance,key,value)
        instance.anime = anime
        return instance
            