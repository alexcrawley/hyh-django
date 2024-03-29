from rest_framework import viewsets

from apps.common import constants
from apps.tickets.models import Ticket
from apps.tickets import serializers


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    queryset = Ticket.objects.order_by('?')
    serializer_class = serializers.TicketSerializer
    paginate_by_param = 'page_size'

    def get_queryset(self):
        return self.request.user.get_tickets()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == constants.CREATE:
            # Contains logic for taking payment from stripe.
            return serializers.CreateTicketSerializer
        else:
            return serializers.TicketSerializer

    def create(self, request, *args, **kwargs):
        user = request.user

        if not user.is_superuser:
            # Users should only be able to create responses for
            # themselves.
            self.request.data.update(**{'user': user.pk})

        return super(TicketViewSet, self).create(request, *args, **kwargs)
