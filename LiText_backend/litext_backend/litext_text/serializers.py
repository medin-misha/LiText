from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import TextBlock


class TextBlockSerializer(ModelSerializer):
    full_text = serializers.SerializerMethodField("get_full_text")

    def get_full_text(self, instance: TextBlock):
        return instance.get_text()

    class Meta:
        model = TextBlock
        fields = "text", "timestamp", "archive", "pk", "full_text"
