from django.shortcuts import render
from .models import Achievement
from .serializer import AchievementSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AchievementView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementRetrieveUpdateDestroy():
    ...


""" def perform_create(self, serializer):
        return serializer.save()
         """