from django.db import models

from apps.constants import LIKE, DISLIKE


class Event(models.Model):
    title = models.CharField(max_length=256)
    img = models.CharField(max_length=256)

    def __unicode__(self):
        return self.title


class EventUserResponse(models.Model):
    RESPONSE_OPTIONS = (
        (LIKE, 'Liked'),
        (DISLIKE, 'Disliked'),
        )

    user = models.ForeignKey('users.User', related_name='event_responses')
    event = models.ForeignKey('events.Event', related_name='user_responses')
    response = models.CharField(max_length=256, choices=RESPONSE_OPTIONS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __unicode__(self):
    #     return self.user.email + ' - ' + self.event

    class Meta:
        unique_together = ('user', 'event')
