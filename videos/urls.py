from django.conf.urls import url
from django.views.generic import ListView, DetailView
from videos.models import Video

urlpatterns = [
        
        url(r'^$', ListView.as_view(
        queryset=Video.objects.all().order_by("-upload_date")[:25],
        template_name="videos/index.html")),


        url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Video,
        template_name="videos/video_post.html")),

        url(r'^$', 'videos.views.video', name='video'),
    ]