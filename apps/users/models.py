from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.constants import LIKE, DISLIKE
from apps.events.models import EventUserResponse


class User(AbstractUser):
    events = models.ManyToManyField(
        'events.Event', through='events.EventUserResponse')

    def __unicode__(self):
        return 'hello'

    def like_event(self, event):
        EventUserResponse.objects.create(
            user=self,
            event=event,
            response=LIKE,
            )

    def dislike_event(self, event):
        EventUserResponse.objects.create(
            user=self,
            event=event,
            response=DISLIKE,
            )

    @property
    def liked_events(self):
        return self.events.filter(user_responses__response=LIKE)

    @property
    def disliked_events(self):
        return self.events.filter(user_responses__response=DISLIKE)
