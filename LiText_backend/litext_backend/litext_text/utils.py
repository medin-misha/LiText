from django.core.exceptions import BadRequest
from celery import shared_task
from django.http import Http404
from django.conf import settings
import requests


def get_text(text: str) -> str:
    response = requests.get(url=settings.TEXT_SAVER_URL + "/api/texts/" + f"one/{text}")
    if 200 <= response.status_code <= 300:
        return response.json()["body"]
    raise Http404(response.json())


def save_text(text: str, user_id: int) -> dict:
    create_text_data: dict = {
        "body": text,
        "user_id": user_id
    }
    response = requests.post(url=settings.TEXT_SAVER_URL + "/api/texts/", json=create_text_data)
    if 200 <= response.status_code <= 300:
        return response.json()
    raise BadRequest(response.json())


@shared_task
def update_text(new_body: str, text: str) -> None:
    update_text_data: dict = {
        "body": new_body
    }
    response = requests.patch(url=settings.TEXT_SAVER_URL + "/api/texts/" + f"{text}", json=update_text_data)
    if 200 <= response.status_code <= 300:
        return
    raise Http404(response.json())


@shared_task
def delete_text(id: str) -> None:
    response = requests.delete(url=settings.TEXT_SAVER_URL + "/api/texts/" + f"{id}")
    if 200 <= response.status_code <= 300:
        return
    raise Http404(response.json())
