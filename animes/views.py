from rest_framework.views import status,Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
import ipdb
from .serializer import AnimeSerializer,AnimeEpisodeAddSerializer,AnimeGenreAddSerializer,AnimeEpisodeAddUpdateSerializer,AnimeGenreAddUpdateSerializer
from episodes.serializer import AnimeEpisodeSerializer
from episodes.serializer import EpisodeSerializer
from genres.serializer import GenreSerializer
from .models import Anime
from episodes.models import Episode
from genres.models import Genre
from .utils import formatQueryParams
from django.shortcuts import get_object_or_404

class AnimesListCreate(ListCreateAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()

    def filter_queryset(self, queryset):
        animes = super().get_queryset()

        query_genre : str = self.request.query_params.get('genre',None)
        query_name : str = self.request.query_params.get('name',None)
        query_start_with : str = self.request.query_params.get('startwith',None)
        
        if query_start_with:
            query_start_with: str = formatQueryParams(query_start_with)
            animes = animes.filter(name__startswith=query_start_with)
        if query_name:
            query_name = formatQueryParams(query_name)
            animes = animes.filter(name__contains=query_name)
        if query_genre:
            query_genre = formatQueryParams(query_genre)
            animes = animes.filter(genres__name__iexact=query_genre)
        return animes

class AnimesHdList(ListAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()

    def get_queryset(self):
        animes = super().get_queryset()
        animes = animes.filter(episodes__video_hd_url__startswith="http")
        return animes
 
class AnimesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()

class EpisodeListCreate(ListCreateAPIView):
    serializer_class = AnimeEpisodeSerializer
    queryset = Episode.objects.all()

class EpisodeRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = AnimeEpisodeSerializer
    queryset = Episode.objects.all()

class GenreListCreate(ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class AnimesEpisodeAdd(CreateAPIView,RetrieveUpdateDestroyAPIView):
    
    queryset = Anime.objects.all()

    def create(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data

        serializer = AnimeEpisodeAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        episode = get_object_or_404(Episode,pk=serializer.validated_data["episode_id"])

        serializer.save(anime=anime,episode=episode)

        serializer = AnimeSerializer(anime)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data

        serializer = AnimeEpisodeAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        is_episode_in_anime = anime.episodes.filter(pk=serializer.validated_data["episode_id"]).exists()
        
        if not is_episode_in_anime:
            msg =  msg = {"detail" : "Anime not have the specify episode"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)

        episode = Episode.objects.get(pk=serializer.validated_data["episode_id"])

        serializer = AnimeEpisodeSerializer(episode)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    
    def partial_update(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data

        serializer = AnimeEpisodeAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        is_episode_in_anime = anime.episodes.filter(pk=serializer.validated_data["episode_id"]).exists()

        if not is_episode_in_anime:
            msg = {"detail" : "Anime not have the specify episode"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)

        episode = Episode.objects.get(pk=serializer.validated_data["episode_id"])

        serializer = AnimeEpisodeAddUpdateSerializer(episode,data,partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data

        serializer = AnimeEpisodeAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        is_episode_in_anime = anime.episodes.filter(pk=serializer.validated_data["episode_id"]).exists()

        if not is_episode_in_anime:
            msg = {"detail" : "Anime not have the specify episode"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)

        Episode.objects.get(pk=serializer.validated_data["episode_id"]).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class AnimesGenreAdd(CreateAPIView,RetrieveUpdateDestroyAPIView):

    queryset = Anime.objects.all()


    def create(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data

        serializer = AnimeGenreAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        genre = get_object_or_404(Genre,pk=serializer.validated_data["genre_id"])

        serializer.save(anime=anime,genre=genre)

        serializer = AnimeSerializer(anime)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data
        
        serializer = AnimeGenreAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        is_genre_in_anime = anime.genres.filter(pk=serializer.validated_data["genre_id"]).exists()

        if not is_genre_in_anime:
            msg = {"detail" : "Anime not have the specify genre"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)

        genre = Genre.objects.get(pk=serializer.validated_data["genre_id"])

        serializer = GenreSerializer(genre)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data

        serializer = AnimeGenreAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        is_genre_in_anime = anime.genres.filter(pk=serializer.validated_data["genre_id"]).exists()

        if not is_genre_in_anime:
            msg = {"detail" : "Anime not have the specify genre"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)

        genre = Genre.objects.get(pk=serializer.validated_data["genre_id"])

        serializer = AnimeGenreAddUpdateSerializer(genre,data=data,partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        anime = self.get_object()

        data = request.data

        serializer = AnimeGenreAddSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        is_genre_in_anime = anime.genres.filter(pk=serializer.validated_data["genre_id"]).exists()

        if not is_genre_in_anime:
            msg = {"detail" : "Anime not have the specify genre"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)

        Genre.objects.get(pk=serializer.validated_data["genre_id"]).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class AnimeGenreRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    