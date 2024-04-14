from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


from .serializers import UserRegisterSerializer, UserSerializer, UserProfileSerializer
from .models import Profile


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

class ProfileView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()  # Make a copy of request data to modify it
        data['user'] = user.pk  # Set the user field based on the authenticated user
        profile = user.profile  # Get the profile associated with the user
        serializer = UserProfileSerializer(instance=profile, data=data)
        if serializer.is_valid():
            serializer.save()
            print(f'First: {profile.first_name}')
            user.first_name = profile.first_name
            user.last_name = profile.last_name
            user.save()
            print(f'User first name: {user.first_name}')
            return Response({
                'Details': 'Data submitted Successfully.',
                'Data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'Error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

