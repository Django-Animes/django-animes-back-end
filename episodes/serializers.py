from rest_framework import serializers
from .models import Episode

class AnimeNameSerializer(serializers.Serializer):
    name = serializers.CharField()

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Episode
        exclude = ("anime",)

    def create(self, validated_data):
        episode = Episode.objects.get_or_create(**validated_data)
        return episode