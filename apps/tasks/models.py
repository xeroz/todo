from django.db import models
from apps.core.models import AuditableModel


class Project(AuditableModel):
    name = models.CharField(max_length=100)


class Incidence(AuditableModel):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Sprint(AuditableModel):
    name = models.CharField(max_length=50)


class Priority(models.Model):
    name = models.CharField(max_length=100)


class StatusTask(models.Model):
    name = models.CharField(max_length=100)


class Task(AuditableModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    estimated_hours = models.IntegerField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    expected_date = models.DateField()
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    incidence = models.ForeignKey(Incidence, on_delete=models.CASCADE)
