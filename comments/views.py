from .models import Comment
from .permissions import IsCommentOwner
from .serializers import CommentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from episodes.models import Episode
from profiles.models import Profile
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class CommentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        profile_id = self.request.data["profile"]
        profile_id = profile_id["id"]
        profile = get_object_or_404(Profile, id=profile_id)
        episode = get_object_or_404(Episode, id=self.kwargs["pk"])
        return serializer.save(profile=profile, episode=episode)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCommentOwner]
    authentication_classes = [JWTAuthentication]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
