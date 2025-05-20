from celery import shared_task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@shared_task
def create_token(user_id: int) -> None:
    Token.objects.create(user=user_id)