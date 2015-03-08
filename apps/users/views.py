from rest_framework import viewsets

from apps.common import constants, permissions
from apps.users.models import User
from apps.users.serializers import (
    UserSerializer,
    RegisterUserSerializer
    )


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    permission_classes = (
        permissions.IsSuperUserOrAnonymous,
    )

    def get_serializer_class(self, *args, **kwargs):
        if self.action == constants.CREATE:
            # Register requires additional validation that the user does
            # not already exist.
            return RegisterUserSerializer
        else:
            return UserSerializer
