from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .models import User
from .serializer import UserSerializer
from .permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class userDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()
