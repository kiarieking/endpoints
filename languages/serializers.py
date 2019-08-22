from rest_framework import serializers
from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
