from django.shortcuts import render
from rest_framework import viewsets, permissions

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'title'
    permission_classes = (IsAuthorOrReadOnly,)
