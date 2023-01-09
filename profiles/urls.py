from django.urls import path
from .views import ProfileListCreate, ProfileUpdateDelete
from comments.views import CommentCreateView, CommentDetailView

urlpatterns = [
    path("user/profile/", ProfileListCreate.as_view()),
    path("user/profile/", ProfileUpdateDelete.as_view()),
    path("comment/<int:pk>/", CommentDetailView.as_view()),
    path("comment/episode/<int:pk>/", CommentCreateView.as_view()),
    path("comment/", CommentDetailView.as_view()),
]
