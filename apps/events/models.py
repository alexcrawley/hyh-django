from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=256)
    img = models.CharField(max_length=256)
