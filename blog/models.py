from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140, null=False)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    post_type = models.CharField(max_length=50, default="normal")

    def __unicode__(self):
        return self.title

