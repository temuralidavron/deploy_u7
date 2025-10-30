from django.urls import path,include
from rest_framework import routers

from project.project_view.project import ProjectModelViewSet, ProjectListAPiView
from project.project_view.task import TaskViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectModelViewSet, basename="projects")
router.register('task', TaskViewSet, basename="task")

urlpatterns = [
    path("",include(router.urls)),
    path('list/',ProjectListAPiView.as_view()),
]