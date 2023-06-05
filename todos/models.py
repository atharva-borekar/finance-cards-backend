from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
