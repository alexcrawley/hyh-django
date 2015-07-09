# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from apps.events.tevo_models import TevoEvent


class Command(BaseCommand):
    def handle(self, *args, **options):
        TevoEvent.objects.update_from_tevo()
