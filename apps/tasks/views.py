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
    # permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PriorityList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        priorities = Priority.objects.all()
        priorities_serializer = PrioritySerializer(priorities, many=True)
        return Response(priorities_serializer.data)

    def post(self, request):
        priorities_serializer = PrioritySerializer(data=request.data)
        if priorities_serializer.is_valid():
            priorities_serializer.save()
            return Response(priorities_serializer.data, status=status.HTTP_201_CREATED)
        return Response(priorities_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PriorityDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Priority.objects.get(pk=pk)
        except Priority.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        priority = self.get_object(pk)
        serializer_priority = PrioritySerializer(priority)
        return Response(serializer_priority.data)

    def put(self, request, pk):
        priority = self.get_object(pk)
        serializer_priority = PrioritySerializer(priority, data=request.data)
        if serializer_priority.is_valid():
            serializer_priority.save()
            return Response(serializer_priority.data)
        return Response(serializer_priority.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        priority = self.get_object(pk)
        priority.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncidenceViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Incidence.objects.all()
    serializer_class = IncidenceSerializer


class SprintViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer


class StatusTaskViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = StatusTask.objects.all()
    serializer_class = StatusTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
