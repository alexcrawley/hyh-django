from rest_framework import viewsets

from apps.events.models import Event
from apps.events.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.order_by('?')
    serializer_class = EventSerializer
    paginate_by_param = 'page_size'
