from django.urls import path
from .views import TextBlockListAPIView, TextBlockDetailView, TextBlockLinkListCreateAPIView, TextBlockLinkDetailAPIView

app_name = "litext-login"

urlpatterns = [
    path("", TextBlockListAPIView.as_view(), name="get-texts-list"),
    path("<int:pk>", TextBlockDetailView.as_view(), name="create-text-block"),
    path("links/", TextBlockLinkListCreateAPIView.as_view(), name="list-create-link"),
    path("links/<str:link>", TextBlockLinkDetailAPIView.as_view(), name="detail-link"),
]
