from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def video(request):
	title = "VIDEOS"
	url = "https://www.youtube.com/embed/97UdoxENO6Q?list=PLei96ZX_m9sWowRU2mn0ccUNIBTTclcWO"
	context = {
		"url": url,
		"title": title,
		}
	return render(request, "videos/index.html", context)

