from django import forms

from polls.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "updated_at"]
