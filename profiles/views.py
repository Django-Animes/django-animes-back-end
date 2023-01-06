from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404
from .permissions import IsAdm, IsAccountOwner
from .serializers import ProfileSerializer, EpisodeWatchSerializer
from episodes.models import Episode
from users.models import User
from .models import Profile


class ProfileCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileWatchEpisodeCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Profile.objects.all()

    def create(self, request, *args, **kwargs):
        profile = self.get_object()
        data = request.data
        user: User = request.user
        is_user_profile_exists = user.profiles.filter(profile).exists()

        if not is_user_profile_exists:
            msg = {"detail": "user not have the specify profile"}
            return Response(data=msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EpisodeWatchSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        episode = get_object_or_404(Episode, pk=serializer.validated_data["episode_id"])

        serializer.save(profile=profile, episode=episode)


class ProfileList(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdm]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
