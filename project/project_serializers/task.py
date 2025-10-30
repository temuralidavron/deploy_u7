from rest_framework import serializers
from project.models import Task


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'assign_to',
            'project'

        ]

    def get_project(self, obj):
        return obj.project.owner.username

