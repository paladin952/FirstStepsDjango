from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=140, null=False)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.title