from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'apps.users'
    verbose_name = 'Users'

    def ready(self):
        from apps.users.signals import *
