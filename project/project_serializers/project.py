from rest_framework import serializers

from project.models import Project, Task
from project.project_serializers.task import TaskSerializer


class ProjectSerializer(serializers.ModelSerializer):
    # task_project=TaskSerializer(read_only=True,many=True)
    email=serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'members',
            'email',
            # "task_project"
        ]

    def get_email(self, obj):
        if obj.owner:
            return obj.owner.email
    #
    # def get_task(self,obj):
    #     project=obj.task_project
    #     return TaskSerializer(project).data

class ProjectListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user_email', read_only=True)
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            # 'owner',
            'user_name',
        ]

    # def get_user_name(self, obj):
    #     if obj.owner:
    #         return obj.owner.username
