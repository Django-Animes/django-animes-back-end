from django.urls import path
from .views import (
    ProfileListCreate,
    ProfileRetrieveUpdateDelete,
    ProfileWatchEpisodeCreate,
)
from comments.views import CommentCreateView, CommentDetailView

urlpatterns = [
    path("user/profile/", ProfileListCreate.as_view()),
    path("user/profile/<int:pk>/", ProfileRetrieveUpdateDelete.as_view()),
    path("user/profile/<int:pk>/watch_episode/", ProfileWatchEpisodeCreate.as_view()),
    path("comment/<int:pk>/", CommentDetailView.as_view()),
    path("comment/episode/<int:pk>/", CommentCreateView.as_view()),
    path("comment/", CommentDetailView.as_view()),
]
