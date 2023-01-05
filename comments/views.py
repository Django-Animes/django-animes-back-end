from .models import Comment
from .serializers import CommentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class CommentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]
    

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
