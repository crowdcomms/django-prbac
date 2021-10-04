from django.apps import AppConfig


class DjangoprbacConfig(AppConfig):
    name = 'django_prbac'

    def ready(self):
        import django_prbac.signals
