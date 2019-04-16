from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'auth'

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
