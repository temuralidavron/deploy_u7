from django.db import models
from common.models import BaseModel



class TaskStatus(models.TextChoices):
    TODO = 'todo', 'TODO'
    IN_PROGRESS = 'in_progress', 'IN_PROGRESS'
    DONE = 'done', 'Done'
    REJECTED = 'rejected', 'Rejected'

class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, related_name='project_own', null=True)
    members = models.ManyToManyField('account.CustomUser', related_name='project_members', blank=True)

    class Meta:
        db_table = 'projects'
        ordering = ('-created_at',)
        # unique_together = ('name','description')

    def __str__(self):
        return self.name





class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=TaskStatus.choices, default=TaskStatus.TODO)
    assign_to = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, related_name='task_assign', null=True)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='task_project')

    class Meta:
        db_table = 'task'
        ordering = ('-created_at',)



    def __str__(self):
        return self.title
