from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .serializers import ProfileSerializer
from .models import Profile


class ProfileListCreate(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileUpdateDelete(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    