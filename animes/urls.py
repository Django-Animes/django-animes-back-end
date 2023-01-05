from django.urls import path
from animes.views import AnimesListCreate,AnimesHdList,AnimesRetrieveUpdateDestroy,EpisodeRetrieveUpdateDestroy,EpisodeList,GenreListCreate,EpisodeCreate,GenreRetrieveUpdateDestroy

urlpatterns = [
    path('animes/',AnimesListCreate.as_view()),
    path('animes/hd/',AnimesHdList.as_view()),
    path('animes/<int:pk>/',AnimesRetrieveUpdateDestroy.as_view()),
    path('animes/episode/',EpisodeList.as_view()),
    path('animes/<int:pk>/episode/',EpisodeCreate.as_view()),
    path('animes/episode/<int:pk>/',EpisodeRetrieveUpdateDestroy.as_view()),
    path('animes/genre/',GenreListCreate.as_view()),
    path("animes/genre/<int:pk>/",GenreRetrieveUpdateDestroy.as_view())
]