from django.contrib import admin

# Register your models here.
from .models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(Video, VideoAdmin)