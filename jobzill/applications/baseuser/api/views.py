from rest_framework.generics import CreateAPIView
from ..models import BaseUser
from .serializer import BaseUserSerializer

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,permissions

class CreateUserView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BaseUserSerializer
    queryset = BaseUser.objects.all()