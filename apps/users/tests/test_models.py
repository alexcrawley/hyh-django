from django.test import TestCase

from apps.users.models import User
from apps.events.models import Event


class TestUserModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testing', password='testing')

    def test_like_event(self):
        self.assertItemsEqual(self.user.liked_events, [])

        event = Event.objects.create(
            title='I like it!', img='Great picture!')

        self.user.like_event(event)

        self.assertEqual(self.user.liked_events.count(), 1)
        self.assertEqual(self.user.liked_events[0], event)

    def test_dislike_event(self):
        self.assertItemsEqual(self.user.disliked_events, [])

        event = Event.objects.create(
            title='I hate it!', img='Horrible picture!')

        self.user.dislike_event(event)

        self.assertEqual(self.user.disliked_events.count(), 1)
        self.assertEqual(self.user.disliked_events[0], event)
