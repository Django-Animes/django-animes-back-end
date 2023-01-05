from .models import Comment
from profiles.models import Profile
from rest_framework import permissions
from rest_framework.views import View, Response


class IsCommentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Comment) -> bool:
        try:
            profile = request.data["profile_id"]
            profile = Profile.objects.get(pk=profile)
            return profile.comments.all().get(obj).exists()
        except Profile.DoesNotExist:
            detail = {"detail": "Profile is not found"}
            return Response(data=detail, status=404)
