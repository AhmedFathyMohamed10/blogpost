from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import *

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
