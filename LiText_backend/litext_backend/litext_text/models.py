from django.db import models
from django.contrib.auth.models import User
from .utils import TextSaver

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
    text_saver = TextSaver()

    def save(self, *args, **kwargs):
        self.text = self.text_saver.save_text(text=self.text, user_id=1)["id"]
        super().save(*args, **kwargs)


    def delete(self, using=None, keep_parents=False):
        self.text_saver.delete_text(id=self.text)
        super().delete(using=using, keep_parents=keep_parents)
