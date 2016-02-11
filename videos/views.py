from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Tutorial
from .models import Video
from .models import TutorialVideos

# Create your views here.
def video(request):
	title = "VIDEOS"

	tutorials_list = Tutorial.objects.all()
	videos_list = Video.objects.all()
	tutorial_videos_list = TutorialVideos.objects.all()

	context = {
		"title": title,
		"tutorials_list": tutorials_list,
		"videos_list": videos_list,
		"tutorial_videos_list": tutorial_videos_list,
		}
	return render(request, "videos/index.html", context)

