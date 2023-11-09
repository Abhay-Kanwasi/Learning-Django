from django.apps import AppConfig


class OnetoonefieldConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OneToOneField'
    def ready(self):
        import OneToOneField.signals