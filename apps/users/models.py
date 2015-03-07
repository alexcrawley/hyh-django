from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.events import constants
from apps.events.models import EventUserResponse


class User(AbstractUser):
    REQUIRED_FIELDS = ['email']

    events = models.ManyToManyField(
        'events.Event', through='events.EventUserResponse')

    def __unicode__(self):
        return 'hello'

    def like_event(self, event):
        EventUserResponse.objects.create(
            user=self,
            event=event,
            response=constants.LIKE,
            )

    def dislike_event(self, event):
        EventUserResponse.objects.create(
            user=self,
            event=event,
            response=constants.DISLIKE,
            )

    @property
    def liked_events(self):
        return self.events.filter(user_responses__response=constants.LIKE)

    @property
    def disliked_events(self):
        return self.events.filter(user_responses__response=constants.DISLIKE)
