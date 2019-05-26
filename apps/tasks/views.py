from apps.tasks.models import (
    Project, Priority, Incidence, Sprint,
    StatusTask, Task)
from apps.tasks.serializers import (
    ProjectSerializer, PrioritySerializer, IncidenceSerializer,
    SprintSerializer, StatusTaskSerializer, TaskSerializer)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PriorityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Priority.objects.all()
    serializer_class = ProjectSerializer


class IncidenceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Incidence.objects.all()
    serializer_class = IncidenceSerializer


class SprintViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer


class StatusTaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StatusTask.objects.all()
    serializer_class = StatusTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
