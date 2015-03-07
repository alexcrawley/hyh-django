from rest_framework import viewsets

from apps.users.models import User
from apps.users.serializers import UserSerializer, RegisterUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            # Register requires additional validation that the user does
            # not already exist.
            return RegisterUserSerializer
        else:
            return UserSerializer
