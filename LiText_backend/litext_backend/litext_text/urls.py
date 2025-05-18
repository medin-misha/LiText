from django.urls import path
from .views import TextBlockListAPIView, TextBlockDetailView

app_name = "litext-login"

urlpatterns = [
    path("", TextBlockListAPIView.as_view(), name="get-texts-list"),
    path("<int:pk>", TextBlockDetailView.as_view(), name="create-text-block"),
]
