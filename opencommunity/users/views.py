from django.shortcuts import render

# Create your views here.
# users/views.py
from requests import Response
from rest_framework import generics

from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

