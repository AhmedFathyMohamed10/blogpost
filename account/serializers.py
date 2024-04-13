from rest_framework import serializers
from django.contrib.auth.models import User


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