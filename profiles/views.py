from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProfileSerializer, EpisodeWatchSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404
from episodes.models import Episode
from users.models import User
from .models import Profile


class ProfileListCreate(CreateAPIView, ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        user = self.request.user
        return user

    def create(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data

        serializer = ProfileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProfileWatchEpisodeCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()

    def create(self, request, *args, **kwargs):
        profile = self.get_object()
        data = request.data
        user: User = request.user

        is_user_profile_exists = user.profiles.filter(pk=profile.id).exists()

        if not is_user_profile_exists:
            msg = {"detail": "user not have the specify profile"}
            return Response(data=msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EpisodeWatchSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        episode = get_object_or_404(Episode, pk=serializer.validated_data["episode_id"])

        serializer.save(profile=profile, episode=episode)

        serializer = ProfileSerializer(profile)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProfileRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        user = self.request.user
        return user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        profile = self.kwargs["pk"]

        is_user_profile_exists = user.profiles.filter(pk=profile).exists()

        if not is_user_profile_exists:
            msg = {"detail": "user not have the specify profile"}
            return Response(data=msg, status=status.HTTP_404_NOT_FOUND)

        profile = Profile.objects.get(pk=profile)

        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        profile = self.kwargs["pk"]
        data = request.data

        is_user_profile_exists = user.profiles.filter(pk=profile).exists()

        if not is_user_profile_exists:
            msg = {"detail": "user not have the specify profile"}
            return Response(data=msg, status=status.HTTP_404_NOT_FOUND)

        profile = Profile.objects.get(pk=profile)

        serializer = ProfileSerializer(profile, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        profile = self.kwargs["pk"]

        is_user_profile_exists = user.profiles.filter(pk=profile).exists()

        if not is_user_profile_exists:
            msg = {"detail": "user not have the specify profile"}
            return Response(data=msg, status=status.HTTP_404_NOT_FOUND)

        profile = Profile.objects.get(pk=profile).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
