from django.db import models
from apps.core.models import AuditableModel
from uuslug import uuslug


class Project(AuditableModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Incidence(AuditableModel):
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)


class Sprint(AuditableModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)


class Priority(models.Model):
    name = models.CharField(max_length=100)


class StatusTask(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(AuditableModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    estimated_hours = models.IntegerField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    expected_date = models.DateField()
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    incidence = models.ForeignKey(Incidence, on_delete=models.CASCADE)
