from rest_framework import viewsets

from apps.common import constants
from apps.events.models import Event, EventUserResponse
from apps.events import serializers


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.order_by('?')
    serializer_class = serializers.EventSerializer
    paginate_by_param = 'page_size'

    def get_queryset(self):
        return self.request.user.get_events()


class EventUserResponseViewSet(viewsets.ModelViewSet):
    queryset = EventUserResponse.objects.all()
    paginate_by_param = 'page_size'

    def get_serializer_class(self, *args, **kwargs):
        if self.action == constants.CREATE:
            # Just require event pk rather than dict.
            return serializers.CreateEventUserResponseSerializer
        else:
            return serializers.EventUserResponseSerializer

    def get_queryset(self):
        queryset = super(EventUserResponseViewSet, self).get_queryset()

        user = self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(user=user)

        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user

        if not user.is_superuser:
            # Users should only be able to create responses for
            # themselves.
            self.request.data.update(**{'user': user.pk})

        return super(EventUserResponseViewSet, self).create(request, *args, **kwargs)
