from .models import Achievement
from rest_framework.views import Response,status
from users.models import User
from .serializer import AchievementSerializer,AchievementUserSerializer,UserAchievementsSerializer,AchievementUserUpdateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
import ipdb

class AchievementListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()

class AchievementUserCreateRetrieveUpdateDestroy(CreateAPIView,RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User,pk=user_id)
        return user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        serializer  = AchievementUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        achievement_id = serializer.validated_data["achievement_id"]
        is_user_achievements_exists = user.achievements.filter(pk=achievement_id).exists()
        if not is_user_achievements_exists:
            msg = {"detail" : "user not have the specify achievement"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)
        achievement = Achievement.objects.get(pk=achievement_id)
        serializer = AchievementSerializer(achievement)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

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
    
    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        serializer  = AchievementUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        achievement_id = serializer.validated_data["achievement_id"]
        is_user_achievements_exists = user.achievements.filter(pk=achievement_id).exists()
        if not is_user_achievements_exists:
            msg = {"detail" : "user not have the specify achievement"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)
        achievement = Achievement.objects.get(pk=achievement_id)
        serializer = AchievementUserUpdateSerializer(achievement,data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        serializer  = AchievementUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        achievement_id = serializer.validated_data["achievement_id"]
        is_user_achievements_exists = user.achievements.filter(pk=achievement_id).exists()
        if not is_user_achievements_exists:
            msg = {"detail" : "user not have the specify achievement"}
            return Response(data=msg,status=status.HTTP_404_NOT_FOUND)
        Achievement.objects.get(pk=achievement_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
