from django.urls import path

from .views import ProjectDetail, ProjectList

urlpatterns = [
    path("", ProjectList.as_view(), name="project_list"),
    path("<int:pk>/", ProjectDetail.as_view(), name="project_detail"),
]
