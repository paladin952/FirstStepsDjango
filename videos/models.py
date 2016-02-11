from django.db import models
from django.utils import timezone

# Create your models here.

class Tutorial(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return str(self.name)


class Video(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=5000)
	upload_date = models.DateTimeField(default=timezone.now)
	url = models.CharField(max_length=500, default="/")
	tags = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return '/video/%s/' % self.id


class TutorialVideos(models.Model):
	tutorial = models.ForeignKey(Tutorial)
	video = models.ForeignKey(Video)
	# my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)

	# class Meta(object):
	# 	ordering = ('my_order',)

	def __unicode__(self):
		return self.tutorial + ": " + self.video

	def __str__(self):
		return str(self.tutorial) + ": " + str(self.video)