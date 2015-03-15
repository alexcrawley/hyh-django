from rest_framework.permissions import BasePermission


class IsSuperUserOrAnonymous(BasePermission):
    """
    Allows access only to anonymous or superusers.
    """

    def has_permission(self, request, view):
        user = request.user
        return user and (user.is_anonymous or user.is_superuser)
