from django.apps import AppConfig


class LitextLoginConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "litext_login"

    def ready(self):
        import litext_login.signals