from rest_framework import permissions
from rest_framework.views import View
from .models import Profile


class IsAdm(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Profile) -> bool:
        return request.user.is_superuser


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Profile) -> bool:
        return request.user.is_authenticated and obj == request.user
