from django.urls import path
from .views import ProjectList
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'tasks'

urlpatterns = [
    path('list', ProjectList.as_view(), name='list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
