from django.db import models
from django import forms
from django.contrib import admin
from .models import Tutorial
from .models import TutorialVideos
from .models import Video

class TutorialModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, tutorial):
		return "%s" % (tutorial.name)

class VideoModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, video):
		return "%s" % (video.title)

class TutorialVideosForms(forms.ModelForm):
	tutorial = TutorialModelChoiceField(queryset=Tutorial.objects.all())
	video = VideoModelChoiceField(queryset=Video.objects.all())
	class Meta:
		model = TutorialVideos
		fields = '__all__'
