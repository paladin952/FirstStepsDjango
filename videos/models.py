from django.db import models
from django.utils import timezone

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=5000)
	upload_date = models.DateTimeField(default=timezone.now)
	video_id = models.CharField(max_length=50)
	tags = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/video/%s/' % self.id