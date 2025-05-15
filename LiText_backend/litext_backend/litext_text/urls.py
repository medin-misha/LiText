from django.urls import path
from .views import ListCreateTextBlockAPIView, RetrieveUpdateDestroyTextBlockAPIView

app_name = "litext-login"

urlpatterns = [
    path("", ListCreateTextBlockAPIView.as_view(), name="create-list-texts"),
    path("<int:pk>", RetrieveUpdateDestroyTextBlockAPIView.as_view(), name="retrieve-update-destroy-texts"),
]
