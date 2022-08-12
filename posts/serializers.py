from rest_framework import serializers

from .models import Post, Comment
from users.serializers import ProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "profile", "post", "text")

class CommentCreateSerializer(serializers.ModelSerializer):
   class Meta:
        model = Comment
        fields = ("post", "text")
    
class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date",
                  "likes", "comment")


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")
        