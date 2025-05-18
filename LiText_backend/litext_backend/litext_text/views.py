from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.http import Http404
from .models import TextBlock
from .serializers import ReturnBlockSerializer, CreateTextBlockSerializer, UpdateTextBlockSerializer


class TextBlockListAPIView(ListCreateAPIView):
    queryset = TextBlock.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateTextBlockSerializer
        return ReturnBlockSerializer



class TextBlockDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TextBlock.objects.all()
    serializer_class = ReturnBlockSerializer

    def put(self, request: Request, pk: int) -> Response:
        model = TextBlock.objects.get(pk=pk)
        if model is None:
            raise Http404("objects is not found")
        print(request.data)
        serializer = UpdateTextBlockSerializer(instance=model, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=model, validated_data=request.data)
        return Response(serializer.data)
