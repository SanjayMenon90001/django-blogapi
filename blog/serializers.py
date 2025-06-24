from rest_framework import serializers
from .models import Post, Comment


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


class CommentSummarySerializer(serializers.ModelSerializer):
    commented_user = serializers.CharField(source='user.username')  # Adjust if your field is different

    class Meta:
        model = Comment
        fields = ['commented_user', 'comment']


class PostCommentsSummarySerializer(serializers.ModelSerializer):
    comments = CommentSummarySerializer(many=True, source='comment_set')
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'comments', 'total_comments']

    def get_total_comments(self, obj):
        return obj.comment_set.count()
