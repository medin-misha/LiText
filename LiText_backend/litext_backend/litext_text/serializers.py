from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import TextBlock, TextBlockLink


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
        fields = "text", "timestamp", "archive", "pk", "user_id"


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


class ReturnTextBlockLinkSerializer(ModelSerializer):
    block = ReturnBlockSerializer(read_only=True)

    class Meta:
        model = TextBlockLink
        fields = "pk", "block_id", "timestamp", "life_time", "link", "block"


class CreateTextBlockLinkSerializer(ModelSerializer):
    class Meta:
        model = TextBlockLink
        fields = "pk", "timestamp", "life_time", "link", "block"
