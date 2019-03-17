from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return Project .objects.create(**validated_data)
