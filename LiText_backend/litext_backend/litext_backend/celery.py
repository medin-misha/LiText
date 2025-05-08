from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "litext_backend.settings")

app = Celery("litext_celery_app")
app.config_from_object(
    "django.conf:settings", namespace="CELERY_"
)
app.autodiscover_tasks()
