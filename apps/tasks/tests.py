from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Priority
from .serializers import PrioritySerializer
import json


class PriorityListApiViewTestCase(APITestCase):
    client = APIClient()

    def setUp(self):
        Priority.objects.create(name='alto')
        Priority.objects.create(name='medio')
        self.url = reverse("tasks:priorities")

    def test_priority_list(self):
        """
            Test to verify priority list
        """
        response = self.client.get(self.url)
        priorities = Priority.objects.all()
        priorities_serializer = PrioritySerializer(priorities, many=True)
        self.assertEqual(response.data, priorities_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_priority_create(self):
        """
            Test to verify priority create
        """
        response = self.client.post(self.url, {'name': 'test'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PriorityDetailApiViewTestCase(APITestCase):
    client = APIClient()

    def setUp(self):
        self.priority = Priority.objects.create(name='bajo')
        self.url = reverse("tasks:priorities_detail", kwargs={"pk": self.priority.pk})

    def test_priority_bundle(self):
        """
            Test to verify priority object bundle
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        priority_serializer = PrioritySerializer(instance=self.priority).data
        response_data = json.loads(response.content)

        self.assertEqual(priority_serializer, response_data)
