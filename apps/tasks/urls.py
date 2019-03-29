from django.urls import path
from .views import ProjectList, ProjectDetail, PriorityList, PriorityDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'tasks'

urlpatterns = [
    path('projects', ProjectList.as_view()),
    path('projects/<int:pk>', ProjectDetail.as_view()),
    path('priorities', PriorityList.as_view(), name='priorities'),
    path('priorities/<int:pk>', PriorityDetail.as_view(), name='priorities_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
