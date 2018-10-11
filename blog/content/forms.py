from django.forms import ModelForm
from content.models import Blog

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ["title", "content"]

