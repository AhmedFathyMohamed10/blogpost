from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class PostSerializer(ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tags', 'created_at', 'author')
        extra_kwargs = {'author': {'write_only': True}, 'tags': {'required': False}}

    def get_author(self, obj):
        return obj.author.username
    
class CommentSerializer(ModelSerializer):
    author = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'author', 'post')

    def get_author(self, obj):
        return obj.author.username
    
    def get_post(self, obj):
        return obj.post.title