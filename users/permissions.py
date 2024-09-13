from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = "Вы не владелец!"

    def has_object_permission(self, request, view, obj):
        return request.user == obj