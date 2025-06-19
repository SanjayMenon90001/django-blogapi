from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from blog.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions
from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'title']


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)