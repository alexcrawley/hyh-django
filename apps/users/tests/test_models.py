from django.test import TestCase

from apps.users.models import User
from apps.events.tests.mixins import EventsTestMixin


class TestUserModel(TestCase, EventsTestMixin):

    def setUp(self):
        self.user = User.objects.create(username='testing', password='testing')

    def test_like_event(self):
        self.assertItemsEqual(self.user.liked_events, [])

        event = self.create_event()

        self.user.like_event(event)

        self.assertEqual(self.user.liked_events.count(), 1)
        self.assertEqual(self.user.liked_events[0], event)

    def test_dislike_event(self):
        self.assertItemsEqual(self.user.disliked_events, [])

        update_kwargs = dict(title='I hate it!', img='Horrible picture!')

        event = self.create_event(**update_kwargs)

        self.user.dislike_event(event)

        self.assertEqual(self.user.disliked_events.count(), 1)
        self.assertEqual(self.user.disliked_events[0], event)
