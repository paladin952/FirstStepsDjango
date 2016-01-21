from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [

    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="blog.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Post,
        template_name="post.html")),

    url(r'^archives$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date"),
        template_name="postTitleList.html")),

    # just the last 5 stories
    url(r'^latestnews', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:5],
        template_name="latestnews.html")),
]
