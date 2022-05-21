from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    # set to current time
    created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    # user who posted the
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
