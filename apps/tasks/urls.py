from django.urls import path, include
from .views import ProjectViewSet, PriorityList, PriorityDetail, IncidenceViewSet
from rest_framework.routers import DefaultRouter

app_name = 'tasks'


router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('incidents', IncidenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('priorities', PriorityList.as_view(), name='priorities'),
    path('priorities/<int:pk>', PriorityDetail.as_view(), name='priorities_detail'),

]
