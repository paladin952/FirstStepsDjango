from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    title = "CLPSTUDIO"
    context = {
        "title": title,
        }
    return render(request, "base.html", context)


def sign_up(request):
    form = SignUpForm(request.POST or None)  # if there is POST data validate it

    # check validation
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print("PRINT " + instance.email)
        print("PRINT " + instance.password)
    else:
        print("Errors: " + str(form.errors))

    title = "SIGN UP"
    context = {
        "title": title,
        "form": form,
    }

    return render(request, "signUp.html", context)


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
