from django.urls import path
from .views import ProjectList, ProjectDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'tasks'

urlpatterns = [
    path('projects', ProjectList.as_view()),
    path('projects/<int:pk>', ProjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
