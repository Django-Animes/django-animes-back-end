from django.urls import path
from animes.views import AnimesListCreate,AnimesHdList,AnimesRetrieveUpdateDestroy,EpisodeRetrieveUpdateDestroy,EpisodeListCreate,GenreListCreate

urlpatterns = [
    path('animes/',AnimesListCreate.as_view()),
    path('animes/hd/',AnimesHdList.as_view()),
    path('animes/<int:pk>/',AnimesRetrieveUpdateDestroy.as_view()),
    path('animes/episode/',EpisodeListCreate.as_view()),
    path('animes/episode/<int:pk>/',EpisodeRetrieveUpdateDestroy.as_view()),
    path('animes/genre/',GenreListCreate.as_view())
]