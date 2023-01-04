from rest_framework.views import status,Response,Request
from rest_framework.generics import ListAPIView,RetrieveAPIView
import ipdb
from .serializer import AnimeSerializer
from .models import Anime
from .utils import formatQueryParams

class AnimesView(ListAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()

    def filter_queryset(self, queryset):
        query_genre : str = self.request.query_params.get('genre',None)
        animes = super().get_queryset()
        if not query_genre:
            return animes
        query_genre = formatQueryParams(query_genre)
        animes = animes.filter(genres__name__iexact=query_genre)
        return animes
        

    