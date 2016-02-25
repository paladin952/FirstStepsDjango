from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Tutorial
from .models import TutorialVideos
from .models import Video


# Create your views here.


def video(request):
    title = "VIDEOS"
    sidebar_title = "All tutorials"

    tutorials_list = Tutorial.objects.all()
    videos_list = Video.objects.all()
    tutorial_videos_list = TutorialVideos.objects.all()

    context = {
        "title": title,
        "tutorials_list": tutorials_list,
        "videos_list": videos_list,
        "tutorial_videos_list": tutorial_videos_list,
        "sidebar_title": sidebar_title,
    }
    return render(request, "videos/index.html", context)


def tutorial_videos(request, tutorial="android"):
    title = "VIDEOS"
    sidebar_title = "All tutorials"

    tutorials_list = Tutorial.objects.all()
    videos_list = Video.objects.all()
    tutorial_videos_list = TutorialVideos.objects.all()

    context = {
        "title": title,
        "tutorials_list": tutorials_list,
        "videos_list": videos_list,
        "tutorial_videos_list": tutorial_videos_list,
        "sidebar_title": sidebar_title,
        "current_tutorial": tutorial.lower(),
    }
    return render(request, "videos/tutorial_videos.html", context)


def video_detail(request, pk=1):
    title = "VIDEOS"
    sidebar_title = "All tutorials"

    tutorials_list = Tutorial.objects.all()
    videos_list = Video.objects.all()
    tutorial_videos_list = TutorialVideos.objects.all()
    video = get_object_or_404(Video, pk=pk)
    context = {
        "title": title,
        "tutorials_list": tutorials_list,
        "videos_list": videos_list,
        "tutorial_videos_list": tutorial_videos_list,
        "sidebar_title": sidebar_title,
        "video": video,
    }
    return render(request, "videos/video_post.html", context)
