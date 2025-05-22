from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from .models import TextBlock
from .serializers import ReturnBlockSerializer, CreateTextBlockSerializer, UpdateTextBlockSerializer
from .permissions import IsOwner

class TextBlockListAPIView(ListCreateAPIView):
    queryset = TextBlock.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateTextBlockSerializer
        return ReturnBlockSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = CreateTextBlockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_block = serializer.save(user_id=request.user.pk)
        return_serializer = ReturnBlockSerializer(instance=new_block)
        return Response({"text_block": return_serializer.data})


class TextBlockDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
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
