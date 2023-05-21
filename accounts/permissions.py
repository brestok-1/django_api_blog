from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username
