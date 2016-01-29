from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.

def home(request):
    return render(request, "base.html", {})


def sign_up(request):
    form = SignUpForm()
    context = {
        "form": form,
    }

    return render(request, "signUp.html", context)
