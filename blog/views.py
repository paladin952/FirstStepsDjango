from django.shortcuts import render

from .forms import ContactForm
from videos.models import Video
from .models import Post

# Create your views here.

def home(request):
    title = "CLPSTUDIO"

    videos_list = Video.objects.all()
    blog_posts_list = Post.objects.all()

    all_site_posts = []
    all_site_posts += videos_list
    all_site_posts += blog_posts_list

    context = {
        "all_site_posts": all_site_posts,
        "title": title,
    }

    return render(request, "base.html", context)


# contact form
def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        # my_email = "clpstudio@outlook.com"
        # subject = "From user" + form_full_name
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [my_email]
        # contact_message = "%s%s via %s"%(form_full_name, form_message, form_email)
        # send_mail(subject,
        #           contact_message,
        #           from_email, to_email,
        #           fail_silently=False)
    title = "CONTACT"
    context = {
        "title": title,
        "form": form,
    }

    return render(request, "contact.html", context)
