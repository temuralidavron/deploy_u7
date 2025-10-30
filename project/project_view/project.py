from rest_framework import viewsets, status, generics
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response

from project.models import Project
from project.permissions import IsOwnerUpdateOrReadOnly
from project.project_serializers.project import ProjectSerializer, ProjectListSerializer


# Create your views here.   CRUD
class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    #
    # def create(self, request, *args, **kwargs):
    #     serializer = ProjectSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(owner=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         return [IsAuthenticated()]
    #     elif self.action=='update':
    #         return [IsOwnerUpdateOrReadOnly()]
    #
    #     return [permission() for permission in self.permission_classes]


class ProjectListAPiView(generics.ListAPIView):
    # queryset = Project.objects.select_related("owner").only('id',
    #                                                         'name',
    #                                                         'description',
    #                                                         'owner_id',
    #
    #                                                         )
    serializer_class = ProjectListSerializer
    def get_queryset(self):
        return Project.objects.select_related('owner').values(
            'id', 'name', 'description', 'owner__email'
        )