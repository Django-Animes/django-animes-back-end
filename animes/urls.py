from django.urls import path
from animes.views import AnimesView,AnimesHdView,AnimesRetrieveUpdateDestroy,EpisodeRetrieveUpdateDestroy

urlpatterns = [
    path('animes/',AnimesView.as_view()),
    path('animes/hd/',AnimesHdView.as_view()),
    path('animes/<int:pk>/',AnimesRetrieveUpdateDestroy.as_view()),
    path('animes/episode/<int:pk>/',EpisodeRetrieveUpdateDestroy.as_view())
]