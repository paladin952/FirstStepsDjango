from django.contrib import admin

# Register your models here.
from .models import Video
from .models import Tutorial
from .models import TutorialVideos
from .forms import TutorialVideosForms

class VideoAdmin(admin.ModelAdmin):
	list_display = ['title']

class TutorialAdmin(admin.ModelAdmin):
	list_display = ['name']

class TutorialVideoAdmin(admin.ModelAdmin):
	form = TutorialVideosForms
	list_display = ['tutorial', 'video']

admin.site.register(Video, VideoAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialVideos, TutorialVideoAdmin)