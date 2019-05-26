from rest_framework import serializers
from .models import (
    Project, Priority, Incidence, Sprint,
    StatusTask, Task)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'slug')


class PrioritySerializer(serializers.Serializer):

    class Meta:
        model = Project
        fields = ('id', 'name')


class IncidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incidence
        fields = ('id', 'slug', 'name', 'project')


class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        fields = ('id', 'slug', 'name')


class StatusTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusTask
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'description',
            'estimated_hours', 'priority', 'expected_date',
            'status', 'status', 'incidence'
        )
