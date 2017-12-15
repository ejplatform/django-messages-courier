from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'You can only modify data about yourself'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user