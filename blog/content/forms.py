from django.forms import ModelForm, Textarea
from content.models import Blog

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ["title", "content"]
        widgets = {
                "content": Textarea(attrs={'cols': 80, 'rows': 20})
                }

