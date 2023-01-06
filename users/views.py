from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from .models import User
from .serializer import UserSerializer
from .permissions import IsAccountOwner, IsAdm, IsYourself
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner, IsAdm]
    
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        user = User.objects.filter(id=self.request.user.id)
        return user
