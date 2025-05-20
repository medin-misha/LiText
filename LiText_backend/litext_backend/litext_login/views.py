from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer