from django.test import TestCase

from rest_framework.reverse import reverse
from rest_framework import status

from apps.events import constants
from apps.events.models import Event, EventUserResponse
from apps.users.models import User


class TestUserEventResponses(TestCase):

    def setUp(self):
        self.regular_user1 = User.objects.create_user(
            username='regular_user1@example.com',
            email='regular_user1@example.com',
            password='testing'
            )

        self.regular_user2 = User.objects.create_user(
            username='regular_user2@example.com',
            email='regular_user2@example.com',
            password='testing'
            )

        self.superuser = User.objects.create_superuser(
            username='superuser@example.com',
            email='superuser@example.com',
            password='testing'
            )

        self.event1 = Event.objects.create(
            title='I like it!', img='Great picture!')

    def test_regular_users_can_only_create_responses_for_themselves(self):
        # Authenticate the request for regular_user1, but try and post with
        # regular_user2 in data. Should ignore regular_user2, and use the
        # authenticated user.

        post_url = reverse('eventuserresponse-list')
        post_data = {
            "user": self.regular_user2.pk,
            "event": self.event1.pk,
            "response": constants.LIKE
        }

        token = self.regular_user1.auth_token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.post(post_url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, EventUserResponse.objects.count())
        self.assertEqual(EventUserResponse.objects.get(
            user=self.regular_user2, event=self.event1))

    def test_superuser_can_create_responses_for_any_user(self):
        # Authenticate the request for superuser, but try and post with
        # regular_user1 in data. Should successfully create response for
        # regular_user1.

        post_url = reverse('eventuserresponse-list')
        post_data = {
            "user": self.regular_user1.pk,
            "event": self.event1.pk,
            "response": constants.LIKE
        }

        token = self.superuser.auth_token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.post(post_url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, EventUserResponse.objects.count())
        self.assertEqual(EventUserResponse.objects.get(
            user=self.regular_user2, event=self.event1))
