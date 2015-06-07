import ticketevolution

from django.conf import settings


class TevoService(object):
    def get_api(self):
        return ticketevolution.Api(
            client_token=settings.TICKET_EVOLUTION_TOKEN,
            client_secret=settings.TICKET_EVOLUTION_SECRET,
            sandbox=settings.TICKET_EVOLUTION_USE_SANDBOX
            )
