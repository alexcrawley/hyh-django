from apps.users.models import Organiser
from apps.events.models import Event


class EventsTestMixin(object):
    def create_organiser(self):
        return Organiser.objects.create(company_name='Test Organiser')

    def create_event(self, **kwargs):
        event_dict = dict(
            title='I like it!',
            img='Great picture!'
        )

        event_dict.update(kwargs)

        return Event.objects.create(**event_dict)
