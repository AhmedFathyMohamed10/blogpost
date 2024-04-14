from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *

from django.shortcuts import get_object_or_404

class CreatePost(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            print(f'The user instance is: {serializer.validated_data['author']}')
            serializer.save()  # Save the post
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePost(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        post = self.get_object()
        if post.author != user:
            raise PermissionDenied("You are not allowed to update this post.")
        serializer.save(author=user)

class DeletePost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated,]

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You don't have permission to delete this post!")
        instance.delete()


class ListPosts(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateComment(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Retrieve the Post instance based on provided post ID
            post_id = request.data.get('post')
            post = Post.objects.get(pk=post_id)
            # Assign the Post instance as the post
            serializer.validated_data['post'] = post
            serializer.validated_data['author'] = request.user
            print(f'Author is: {serializer.validated_data['author']}')
            print(f'Post is: {serializer.validated_data['post']}')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateComment(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        comment = self.get_object()
        author = self.request.user 
        # Only user can update its own comment
        if comment.author != author:
            raise PermissionDenied("You are not allowed to update this comment.")
        serializer.save(author=author)

class DestroyComment(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_destroy(self, instance):
        comment = self.get_object()
        author = self.request.user
        if comment.author != author:
            raise PermissionDenied("You don't have permission to delete this comment!")
        instance.delete()


        