from django.test import TestCase

from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.events import constants
from apps.events.models import EventUserResponse
from apps.events.tests.mixins import EventsTestMixin
from apps.users.models import User


class TestUserEventResponses(TestCase, EventsTestMixin):

    def setUp(self):
        self.client = APIClient()

        self.event1 = self.create_event()

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
        self.assertTrue(EventUserResponse.objects.filter(
            user=self.regular_user1.pk, event=self.event1.pk).exists())

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
        self.assertTrue(EventUserResponse.objects.filter(
            user=self.regular_user1.pk, event=self.event1.pk).exists())

    def test_regular_users_can_only_view_their_own_responses(self):
        user1_event = EventUserResponse.objects.create(
            user=self.regular_user1,
            event=self.event1,
            response=constants.LIKE
            )

        EventUserResponse.objects.create(
            user=self.regular_user2,
            event=self.event1,
            response=constants.LIKE
            )

        get_url = reverse('eventuserresponse-list')
        token = self.regular_user1.auth_token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.get(get_url, {}, format='json')

        expected_reponse_data = [
            {
                "id": user1_event.pk,
                "user": self.regular_user1.pk,
                "event": {
                    'id': self.event1.pk,
                    'title': self.event1.title,
                    'img': self.event1.img
                    },
                "response": constants.LIKE
            },
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'], expected_reponse_data)

    def test_superusers_can_view_all_responses(self):
        user1_event = EventUserResponse.objects.create(
            user=self.regular_user1,
            event=self.event1,
            response=constants.LIKE
            )

        user2_event = EventUserResponse.objects.create(
            user=self.regular_user2,
            event=self.event1,
            response=constants.LIKE
            )

        get_url = reverse('eventuserresponse-list')
        token = self.superuser.auth_token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.get(get_url, {}, format='json')

        expected_reponse_data = [
            {
                "id": user2_event.pk,
                "user": self.regular_user2.pk,
                "event": {
                    'id': self.event1.pk,
                    'title': self.event1.title,
                    'img': self.event1.img
                    },
                "response": constants.LIKE
            },
            {
                "id": user1_event.pk,
                "user": self.regular_user1.pk,
                "event": {
                    'id': self.event1.pk,
                    'title': self.event1.title,
                    'img': self.event1.img
                    },
                "response": constants.LIKE
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'], expected_reponse_data)
