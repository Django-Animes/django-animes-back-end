from rest_framework.permissions import SAFE_METHODS
from rest_framework import permissions


class IsAdm(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser
