from django.conf.urls import url
from django.views.generic import ListView, DetailView
from videos.models import Video
from videos.models import TutorialVideos

urlpatterns = [
        

        url(r'^(?P<pk>\d+)$', 'videos.views.video_detail', name="video_detail"),


        url(r'^tutorials/(?P<tutorial>.+)$', 'videos.views.tutorial_videos', name='tutorial_videos'),


        url(r'^$', 'videos.views.video', name='video'),
    ]