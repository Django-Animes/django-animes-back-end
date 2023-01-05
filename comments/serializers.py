from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = [
            "id",
            "update_at",
            "created_at",
        ]


def create(self, validated_data):
    comment = Comment.objects.get_or_create(**validated_data)
    return comment
