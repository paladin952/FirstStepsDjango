from django import forms
from .models import Post
from .models import SignUp


# post something on the site form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        self.validate_title(title)
        return title

    @staticmethod
    def validate_title(title):
        if len(title) <= 3:
            raise forms.ValidationError("The tile is to short. Use a title that has at least 3 characters")


# login form
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'password']