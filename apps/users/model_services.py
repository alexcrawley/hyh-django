#-*- coding: utf-8 -*-

from apps.events.models import EventUserResponse
from apps.events import constants as events_constants

from apps.experiments.models import TestGroup
from apps.experiments import constants as experiments_constants
from apps.experiments.event_algorithms import algorithms


class UserEventService(object):
    """ Encapsulate services relating users and event.
    """
    def get_events(self):
        test_group = TestGroup.objects.get_for_experiment(
            user=self,
            experiment_type=experiments_constants.EVENTS_ALGORITHM_EXPERIMENT
            )

        return algorithms[test_group.algorithm]().get_events_for_user(self)

    def like_event(self, event):
        return EventUserResponse.objects.create(
            user=self,
            event=event,
            response=events_constants.LIKE,
            )

    def dislike_event(self, event):
        return EventUserResponse.objects.create(
            user=self,
            event=event,
            response=events_constants.DISLIKE,
            )

    @property
    def liked_events(self):
        return self.events.filter(
            user_responses__response=events_constants.LIKE)

    @property
    def disliked_events(self):
        return self.events.filter(
            user_responses__response=events_constants.DISLIKE)


class UserTicketService(object):
    """ Encapsulate services relating users and tickets.
    """
    def get_tickets(self):
        return self.tickets.all()


class UserServices(UserEventService, UserTicketService):
    """ Container for all user service mixins.
    """
    pass
