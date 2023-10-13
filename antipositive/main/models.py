from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
