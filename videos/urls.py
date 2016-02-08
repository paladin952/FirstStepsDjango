from django.conf.urls import url
from django.views.generic import ListView, DetailView
from videos.models import Video

urlpatterns = [

        url(r'^$', 'videos.views.video', name='video'),

    ]