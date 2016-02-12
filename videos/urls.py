from django.conf.urls import url
from django.views.generic import ListView, DetailView
from videos.models import Video
from videos.models import TutorialVideos

urlpatterns = [
        

        url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Video,
        template_name="videos/video_post.html")),


        url(r'^tutorials/(?P<tutorial>.+)$', 'videos.views.tutorial_videos', name='tutorial_videos'),


        url(r'^$', 'videos.views.video', name='video'),
    ]