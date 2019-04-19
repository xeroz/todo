from apps.tasks.models import Project, Priority, Incidence
from apps.tasks.serializers import ProjectSerializer, PrioritySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ProjectList(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return Response(projects_serializer.data)

    def post(self, request):
        projects_serializer = ProjectSerializer(data=request.data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return Response(projects_serializer.data, status=status.HTTP_201_CREATED)
        return Response(projects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer_project = ProjectSerializer(project)
        return Response(serializer_project.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer_project = ProjectSerializer(project, data=request.data)
        if serializer_project.is_valid():
            serializer_project.save()
            return Response(serializer_project.data)
        return Response(serializer_project.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PriorityList(APIView):
    # permission_classes = (IsAuthenticated,)

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
    # permission_classes = (IsAuthenticated,)

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


class IncidenceList(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        incidence = Incidence.objects.all()
        incidences_serializer = PrioritySerializer(incidence, many=True)
        return Response(incidences_serializer.data)

    def post(self, request):
        priorities_serializer = PrioritySerializer(data=request.data)
        if priorities_serializer.is_valid():
            priorities_serializer.save()
            return Response(priorities_serializer.data, status=status.HTTP_201_CREATED)
        return Response(priorities_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
