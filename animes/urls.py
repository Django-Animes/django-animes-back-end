from django.urls import path
from . import views

urlpatterns = [
    path('animes/',views.AnimesListCreate.as_view()),
    path('animes/hd/',views.AnimesHdList.as_view()),
    path('animes/<int:pk>/',views.AnimesRetrieveUpdateDestroy.as_view()),
    path('animes/episode/',views.EpisodeListCreate.as_view()),
    path('animes/<int:pk>/episode/',views.AnimesEpisodeAdd.as_view()),
    path('animes/episode/<int:pk>/',views.EpisodeRetrieveUpdateDestroy.as_view()),
    path('animes/genre/',views.GenreListCreate.as_view()),
    path('animes/<int:pk>/genre/',views.AnimesGenreAdd.as_view())
]