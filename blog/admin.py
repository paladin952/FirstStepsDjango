from django.contrib import admin
from .models import Post
from .models import SignUp
from .forms import PostForm
from .forms import SignUpForm


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "date"]
    form = PostForm


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "password"]
    form = SignUpForm


admin.site.register(Post, PostAdmin)
admin.site.register(SignUp, SignUpAdmin)
