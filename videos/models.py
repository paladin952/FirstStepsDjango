from django.db import models
from django.utils import timezone

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=5000)
	upload_date = models.DateTimeField(default=timezone.now)
	url = models.CharField(max_length=500, default="/")
	tags = models.CharField(max_length=200)
	video_type = models.CharField(max_length=50, default="normal")
	bla = models.CharField(max_length=200, default="blabla")

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/video/%s/' % self.id