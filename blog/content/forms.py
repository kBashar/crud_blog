from django.forms import ModelForm, Textarea
from content.models import Blog
from .offensive import check_offensive

class BlogForm(ModelForm):
    
    def clean_title(self):
            data = self.cleaned_data["title"]
            return check_offensive(data)

    def clean_content(self):
        data = self.cleaned_data["content"]
        return check_offensive(data)
    

        
    class Meta:
        model = Blog
        fields = ["title", "content"]
        widgets = {
                "content": Textarea
                }

