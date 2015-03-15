from django.db import models


class Ticket(models.Model):
    event = models.ForeignKey('events.Event', related_name='tickets')
    user = models.ForeignKey('users.User', related_name='tickets')
