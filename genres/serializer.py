from rest_framework import serializers
from .models import Genre
class GenreSerializer(serializers.ModelSerializer):
    class Meta():
        model = Genre
        fields = "__all__"
    
    def create(self,validated_data: dict):
        genre = validated_data['name']
        genre,_ = Genre.objects.get_or_create(name=genre)
        return genre