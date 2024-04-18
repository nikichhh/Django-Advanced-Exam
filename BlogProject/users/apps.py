from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'BlogProject.users'

    def ready(self):
        from . import signals
