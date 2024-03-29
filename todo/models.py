from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TasksModel(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date = models.DateField()

    def __str__(self):
        return self.name