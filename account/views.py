from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import UserRegisterSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import authentication


class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            if not User.objects.filter(username=username).exists():
                password = make_password(serializer.validated_data.get('password'))
                User.objects.create(
                    email=serializer.validated_data.get('email'),
                    username=username,
                    password=password
                )
                return Response({'Details': 'Your account has been created successfully!'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'Error': 'This credentials already exist!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GetUsers(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )