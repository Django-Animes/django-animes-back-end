from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProfileSerializer
from .models import Profile


class ProfileListCreate(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # authentication - JWT

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileUpdateDelete(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # authentication - JWT

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
