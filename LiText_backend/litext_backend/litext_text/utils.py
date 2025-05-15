from django.core.exceptions import BadRequest
from django.http import Http404
from django.conf import settings
import requests


class TextSaver:
    protocol: str = "http://"
    url: str = settings.TEXT_SAVER_URL
    path: str = "/api/texts/"

    def save_text(self, text: str, user_id: int) -> dict:
        create_text_data: dict = {
            "body": text,
            "user_id": user_id
        }
        response = requests.post(url=self.protocol + self.url + self.path, json=create_text_data)
        if 200 <= response.status_code <= 300:
            return response.json()
        raise BadRequest(response.json())


    def delete_text(self, id: str) -> None:
        response = requests.delete(url=self.protocol + self.url + self.path + f"{id}")
        print(response.status_code)
        if 200 <= response.status_code <= 300:
            return
        raise Http404(response.json())