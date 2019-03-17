from apps.tasks.models import Project
from apps.tasks.serializers import ProjectSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return Response(projects_serializer.data)

    def post(self, request, format=None):
        projects_serializer = ProjectSerializer(data=request.data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return Response(projects_serializer.data, status=status.HTTP_201_CREATED)
        return Response(projects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer_project = ProjectSerializer(project)
        return Response(serializer_project.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer_project = ProjectSerializer(project, data=request.data)
        if serializer_project.is_valid():
            serializer_project.save()
            return Response(serializer_project.data)
        return Response(serializer_project.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
