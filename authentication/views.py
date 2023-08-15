from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import get_user_model

User=get_user_model()
# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class=serializers.UserSerializer
