from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from .serializers import LanguageSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate


# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LanguageSerializer



