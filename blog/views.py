from django.shortcuts import render
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from blog.models import Comment, Post
# Create your views here.
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["author", "title"]
    lookup_field = 'slug'


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'], url_path='comments', permission_classes=[IsAdminUser])
    def comments(self, request, slug=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response({
            "post_id": post.id,
            "comments": serializer.data,
            "total_comments": comments.count()
        })


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


