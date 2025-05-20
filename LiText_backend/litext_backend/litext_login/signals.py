from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import create_token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance: User = None, created: bool = False, **kwargs):
    if created:
        create_token.delay(instance.pk)