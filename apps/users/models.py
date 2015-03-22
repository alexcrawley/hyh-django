from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.events import constants as events_constants
from apps.events.models import EventUserResponse

from apps.experiments.models import TestGroup
from apps.experiments import constants as experiments_constants
from apps.experiments.event_algorithms import algorithms


class User(AbstractUser):
    REQUIRED_FIELDS = ['email']

    events = models.ManyToManyField(
        'events.Event', through='events.EventUserResponse')

    def __unicode__(self):
        return self.username

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


class Organiser(models.Model):
    company_name = models.CharField(max_length=256)
