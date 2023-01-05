from rest_framework.views import status,Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
import ipdb
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import AnimeSerializer
from episodes.serializer import EpisodeSerializer
from genres.serializer import GenreSerializer
from .models import Anime
from episodes.models import Episode
from genres.models import Genre
from .utils import formatQueryParams
from .permissions import AnimeListCreatePermission

class AnimesListCreate(ListCreateAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()
    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]

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

    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        animes = super().get_queryset()
        animes = animes.filter(episodes__video_hd_url__startswith="http")
        return animes
 
class AnimesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()
    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]

class EpisodeList(ListAPIView):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]

class EpisodeCreate(CreateAPIView):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            anime_id = kwargs['pk']
            anime = Anime.objects.get(pk=anime_id)
            serializer = EpisodeSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(anime=anime)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        except Anime.DoesNotExist:
            msg = {"detail" : "Anime not found."}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)

       
class EpisodeRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]

class GenreListCreate(ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]

class GenreRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    permission_classes = [AnimeListCreatePermission]
    authentication_classes = [JWTAuthentication]
    