from django.db import models
from datetime import datetime


class AuditableModel(models.Model):
    created = models.DateTimeField(editable=False, blank=True, default=datetime.now)
    modified = models.DateTimeField(editable=False, blank=True, default=datetime.now)
    created_by = models.IntegerField('Created by', editable=False, null=True,
                                     default=0)
    modified_by = models.IntegerField('Modified by', editable=False,
                                      null=True, default=0)

    class Meta:
        abstract = True
