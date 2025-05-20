from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import TextBlock


class ReturnBlockSerializer(ModelSerializer):
    body = serializers.SerializerMethodField("get_full_text")

    def get_full_text(self, instance: TextBlock):
        return instance.get_text()

    class Meta:
        model = TextBlock
        fields = "timestamp", "archive", "pk", "body"


class CreateTextBlockSerializer(ModelSerializer):
    class Meta:
        model = TextBlock
        fields = "text", "timestamp", "archive", "pk"


class UpdateTextBlockSerializer(ModelSerializer):
    body = serializers.SerializerMethodField("get_full_text")

    def get_full_text(self, instance: TextBlock):
        return instance.get_text()

    def update(self, instance: TextBlock, validated_data: dict):
        instance.update(new_body=validated_data["body"])
        return instance
    class Meta:
        model = TextBlock
        fields = "body",
