from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs = {"pk":self.id})

    class Meta:
        ordering = ['-date_published']
