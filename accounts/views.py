from django.contrib.auth import get_user_model
from rest_framework import viewsets

from accounts.permissions import IsUserOrReadOnly
from accounts.serializers import UserSerializer


# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsUserOrReadOnly,)
