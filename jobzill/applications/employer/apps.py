from django.apps import AppConfig


class EmployerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobzill.applications.employer'

    # def ready(self):
    #     from . import signals