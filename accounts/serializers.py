from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'id')
        lookup_field = 'username'
        model = get_user_model()
