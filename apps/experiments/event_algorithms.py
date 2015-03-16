from apps.experiments import constants
from apps.events.models import Event


class RandomEvents(object):
    def get_events_for_user(self, user, quantity=None):
        events = Event.objects.order_by('?')

        if quantity is not None:
            events = events[:quantity]

        return events


algorithms = {
    constants.DEFAULT_EVENTS_ALGORITHM: RandomEvents,
    constants.RANDOM_EVENTS_ALGORITHM: RandomEvents,
    }
