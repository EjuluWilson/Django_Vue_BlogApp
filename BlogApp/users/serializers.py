from rest_framework import serializers
from .models import UserModel


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username"]