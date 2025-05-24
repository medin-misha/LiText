from django.core.exceptions import BadRequest
from .tasks import update_text, delete_text, delete_hash
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


def get_hash(text: str, life_time: int | None) -> str:
    data: dict = {"string": text, "timeout": 10 ** 10 if life_time is None else life_time}
    print(data)
    response = requests.post(url=settings.HESHAROR_URL + "/api/v1/hash", json=data)
    if 200 <= response.status_code <= 300:
        return response.json()["hash"]
    raise BadRequest(response.json())
