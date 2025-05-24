from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.mixins import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from django.http import Http404
from .models import TextBlock, TextBlockLink
from .serializers import ReturnBlockSerializer, CreateTextBlockSerializer, UpdateTextBlockSerializer, \
    ReturnTextBlockLinkSerializer, CreateTextBlockLinkSerializer
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


class TextBlockLinkListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = TextBlockLink.objects.all()
    serializer_class = CreateTextBlockLinkSerializer


class TextBlockLinkDetailAPIView(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = TextBlockLink.objects.select_related("block").all()
    serializer_class = ReturnTextBlockLinkSerializer

    def get(self, request: Request, link: str) -> Response:
        link_instance = TextBlockLink.objects.select_related("block").get(link=link)
        serializer = ReturnTextBlockLinkSerializer(instance=link_instance)
        return Response(serializer.data)

    def delete(self, request, link: str) -> Response:
        link_instance = TextBlockLink.objects.get(link=link)
        link_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
