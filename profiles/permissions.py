from rest_framework import permissions
from .models import Profile


class ProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, _, obj: Profile) -> bool:
        return request.user.is_authenticated and obj == request.user
