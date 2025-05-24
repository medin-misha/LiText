from celery import shared_task
from django.http import Http404
from django.conf import settings
import requests


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


@shared_task
def delete_hash(hash: str) -> None:
    response = requests.delete(url=settings.HESHAROR_URL + "/api/v1/hash" + hash)
    if 200 <= response.status_code <= 300:
        return
    raise Http404(response.json())