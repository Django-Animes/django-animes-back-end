from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from .models import User
from .serializer import UserSerializer
from .permissions import IsAccountOwner, IsAdm
from rest_framework_simplejwt.authentication import JWTAuthentication
from achievements.models import Achievement
from django.shortcuts import get_object_or_404
from .serializer import UserSerializer
import ipdb



class UserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserListView(ListAPIView):
    permission_classes = [IsAdm]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class AchievementUpdateView(APIView):
    def patch(self, request, user_id):
        cu = get_object_or_404(Achievement, id=request.data["achievements"][0]["id"])
        
        user = get_object_or_404(User, id = user_id)
        
        serializer = UserSerializer(user, data = request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save(achievements = cu)
        return Response(serializer.data)
