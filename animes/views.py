from rest_framework.views import status,Response,Request
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
import ipdb
from .serializer import AnimeSerializer
from episodes.serializer import EpisodeSerializer
from genres.serializer import GenreSerializer
from .models import Anime
from episodes.models import Episode
from genres.models import Genre
from .utils import formatQueryParams

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
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

class EpisodeRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

class GenreListCreate(ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    