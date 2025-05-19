from django.db import models
from django.contrib.auth.models import User
from .utils import get_text, save_text, update_text, delete_text

# Create your models here.
"""
TextBlock
- id
- user
- text
- timestamp
- archive
"""


class TextBlock(models.Model):
    # user = models.ForeignKey(to=User, on_delete=models.CASCADE())
    text = models.CharField()
    timestamp = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.text = save_text(text=self.text, user_id=1)["id"]
        super().save(*args, **kwargs)

    def update(self, new_body: str) -> None:
        update_text.delay(new_body=new_body, text=self.text)

    def delete(self, using=None, keep_parents=False):
        delete_text.delay(id=self.text)
        super().delete(using=using, keep_parents=keep_parents)

    def get_text(self):
        self.full_text = get_text(text=self.text)
        return self.full_text
