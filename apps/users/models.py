from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.model_services import UserServices


class User(AbstractUser, UserServices):
    REQUIRED_FIELDS = ['email']

    events = models.ManyToManyField(
        'events.Event', through='events.EventUserResponse')

    def __unicode__(self):
        return self.username


class Organiser(models.Model):
    company_name = models.CharField(max_length=256)
