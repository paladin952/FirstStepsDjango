from django import forms

from .models import Post


# post something on the site form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'date', 'post_type']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        self.validate_title(title)
        return title

    @staticmethod
    def validate_title(title):
        if len(title) <= 3:
            raise forms.ValidationError("The tile is to short. Use a title that has at least 3 characters")

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
