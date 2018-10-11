from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import (
        LoginRequiredMixin,
        UserPassesTestMixin
        )
from django.urls import reverse_lazy


from content.models import Blog
from content.forms import BlogForm


class BlogList(ListView):
    model = Blog
    template_name = "content/bloglist.html"

class BlogDetail(DetailView):
    model = Blog
    template_name="content/blogdetail.html"

class BlogCreate(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name="content/blogcreate.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name="content/blogcreate.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

class LogIn(LoginView):
    template_name = "content/login.html"
    
class LogOut(LogoutView):
    template_name = "content/base.html"
    success_url = reverse_lazy("home")
