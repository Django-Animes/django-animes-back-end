from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user


class IsAdm(permissions.BasePermission):
    def has_permission(self, request, view):

        user = request.user

        if user and user.is_superuser:
            return True
        return False


class IsYourself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return obj.id == request.user.id
