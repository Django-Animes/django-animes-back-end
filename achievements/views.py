from django.shortcuts import render
from .models import Achievement
from rest_framework.views import Response
from users.models import User
from .serializer import AchievementSerializer,AchievementUserSerializer,UserAchievementsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
import ipdb

class AchievementView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()

class AchievementUserCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User,pk=user_id)
        return user

    def create(self, request, *args, **kwargs):
        data = request.data
        user = self.get_object()
        serializer = AchievementUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        achievement_id = serializer.validated_data['achievement_id']
        achievement = get_object_or_404(Achievement,pk=achievement_id)
        serializer.save(user=user,achievement=achievement)
        serializer = UserAchievementsSerializer(user)
        return Response(data=serializer.data,status=200)



