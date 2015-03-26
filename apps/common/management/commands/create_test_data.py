# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from apps.events.models import Event
from apps.users.models import User, Organiser


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_users()
        self.create_events()
        self.like_events()

    def create_users(self):
        try:
            User.objects.get(username='regular')
        except User.DoesNotExist:
            User.objects.create_user(
                username='regular',
                email='regular@example.com',
                password='testing'
                )

        try:
            User.objects.get(username='superuser')
        except User.DoesNotExist:
            User.objects.create_superuser(
                username='superuser',
                email='superuser@example.com',
                password='testing'
                )

    def create_events(self):
        organiser = Organiser.objects.create(company_name='Test Organiser')

        Event.objects.create(
            organiser=organiser,
            title='Firework tonight!',
            img='http://www.mathforgrownups.com/wp-content/uploads/2012/06/firework.jpg.pagespeed.ce.Fh58gK_YoW.jpg'
            )
        Event.objects.create(
            organiser=organiser,
            title='Fine dining..',
            img='http://www.tablespoon.com/~/media/Images/Articles/qd/2011/07/2011-07-25-monster-veggie-burger-500.jpg'
            )
        Event.objects.create(
            organiser=organiser,
            title='Rooftop cinema?',
            img='http://1.bp.blogspot.com/-2SzFzltjliM/Ua8oFQuBviI/AAAAAAAAADM/w7mOBWrbT-8/s1600/RooftopFilmClub.jpg'
            )

    def like_events(self):
        for user in User.objects.all():
            for event in Event.objects.all():
                user.like_event(event)
