from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Comment, Post
# Create your views here.
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import CommentSerializer, PostSerializer
from django.utils.text import slugify


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["author", "title"]
    lookup_field = 'slug'


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .models import Post, Comment

class AdminAuthorPostSummary(APIView):
    permission_classes = [IsAdminUser]  # Only superusers can access

    def get(self, request):
        author_username = request.query_params.get('author')
        if not author_username:
            return Response({"error": "Author username is required."}, status=400)

        try:
            author = User.objects.get(username=author_username)
        except User.DoesNotExist:
            return Response({"error": "Author not found"}, status=404)
        posts = Post.objects.filter(author=author)
        result = []
        for post in posts:
            comments = Comment.objects.filter(post=post)
            comment_data = [
                {"commented_user": c.author.username, "comment": c.content}
                for c in comments
            ]
            result.append({
                "post_id": post.slug,
                "title": post.title,
                "comments": comment_data,
                "total_comments": comments.count()
            })
        return Response(result)
