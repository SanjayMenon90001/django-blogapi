from rest_framework import serializers

from blog.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Nested comments

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['slug', 'author', 'created']
