from django.apps import AppConfig


class MailServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_service'

    def ready(self):
        from mail_service.scheduler_job import updater
        updater.start()