from django.apps import AppConfig


class RejLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rej_log'

    def ready(self):
        import rej_log.signals
        