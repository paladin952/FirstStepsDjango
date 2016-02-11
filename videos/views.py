from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def video(request):
	title = "VIDEOS"
	video_list = Video.objects.all()

	video_type_list = video_list

	context = {
		"title": title,
		"video_type_list": video_type_list
		}
	return render(request, "videos/index.html", context)

