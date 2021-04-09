from django.db import models
import datetime
# Create your models here.


class List(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, default="")
    updated_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField()
    parrent = models.ForeignKey(List, on_delete=models.CASCADE,null=True, related_name="tasks")

    def __str__(self):
        return self.title
