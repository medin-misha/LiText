from rest_framework.serializers import ModelSerializer
from .models import TextBlock
class TextBlockSerializer(ModelSerializer):
    class Meta:
        model = TextBlock
        fields = "text", "timestamp", "archive", "pk"