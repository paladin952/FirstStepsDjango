from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=140, null=False)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    post_type = models.CharField(max_length=50, default="normal")

    def __unicode__(self):
        return self.title


class SignUp(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False)

    def __unicode__(self):
        return self.email
