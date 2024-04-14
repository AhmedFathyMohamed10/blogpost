from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        extra_kwargs = {
            'email' : {'required':True ,'allow_blank':False},
            'password' : {'required':True ,'allow_blank':False,'min_length':8}
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username', 'email')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = ('user', 'first_name', 'last_name', 'age')