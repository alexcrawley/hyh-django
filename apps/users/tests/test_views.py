from django.test import TestCase

from rest_framework.reverse import reverse
from rest_framework import status

from apps.users import constants
from apps.users.models import User


class TestRegisterUser(TestCase):

    def test_valid_data_creates_user_and_returns_token(self):
        post_url = reverse('user-list')
        post_data = {
            'email': 'test@example.com',
            'password1': 'testing',
            'password2': 'testing',
        }

        response = self.client.post(post_url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], post_data['email'])
        self.assertIsNotNone(response.data['auth_token'])

        self.assertTrue(
            User.objects.get(auth_token=response.data['auth_token'])
            )

    def test_validate_passwords_match(self):
        post_url = reverse('user-list')
        post_data = {
            'email': 'test@example.com',
            'password1': 'blah',
            'password2': 'differentblah',
        }

        response = self.client.post(post_url, post_data, format='json')

        expected_response_data = {
            "non_field_errors": [
                constants.PASSWORDS_DO_NOT_MATCH
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_data)

        # Check no user created.
        self.assertEqual(0, User.objects.count())

    def test_user_with_email_does_not_exist(self):
        user = User.objects.create_user(
            email='test@example.com',
            username='test@example.com',
            password='testing'
            )

        post_url = reverse('user-list')
        post_data = {
            'email': 'test@example.com',
            'password1': 'testing',
            'password2': 'testing',
        }

        response = self.client.post(post_url, post_data, format='json')

        expected_response_data = {
            "email": [
                constants.USER_WITH_EMAIL_EXISTS
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_data)

        # First user is still the only user.
        self.assertEqual(User.objects.get(), user)


class TestAuthToken(TestCase):
    def test_get_token_for_user(self):
        user = User.objects.create_user(
            email='test@example.com',
            username='test@example.com',
            password='testing'
            )

        post_url = reverse('api_token_auth')
        post_data = {
            'email': 'test@example.com',
            'username': 'test@example.com',
            'password': 'testing',
        }

        response = self.client.post(post_url, post_data, format='json')

        expected_response_data = {
            "token": user.auth_token.key
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response_data)
