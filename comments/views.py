from .models import Comment
from .permissions import IsCommentOwner
from .serializers import CommentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class CommentView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCommentOwner]
    authentication_classes = [JWTAuthentication]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
