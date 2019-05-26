from django.urls import path, include
from .views import (
    ProjectViewSet, PriorityViewSet,
    IncidenceViewSet, SprintViewSet, StatusTaskViewSet,
    TaskViewSet)
from rest_framework.routers import DefaultRouter

app_name = 'tasks'


router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('incidents', IncidenceViewSet)
router.register('sprints', SprintViewSet)
router.register('status-task', StatusTaskViewSet)
router.register('tasks', TaskViewSet)
router.register('priorities', PriorityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
