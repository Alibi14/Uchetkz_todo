from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey('userauth.User', on_delete=models.CASCADE, null=True)
