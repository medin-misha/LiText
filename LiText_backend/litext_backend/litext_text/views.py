from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import TextBlock
from .serializers import TextBlockSerializer

class ListCreateTextBlockAPIView(ListCreateAPIView):
    queryset = TextBlock.objects.all()
    serializer_class = TextBlockSerializer


class RetrieveUpdateDestroyTextBlockAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TextBlock.objects.all()
    serializer_class = TextBlockSerializer