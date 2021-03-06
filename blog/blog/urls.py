"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from content.views import (
        BlogList, 
        BlogDetail, 
        BlogCreate, 
        LogIn,
        LogOut, 
        BlogUpdate, 
        BlogDelete
        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', BlogList.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetail.as_view(), name="blog_detail"),
    path('blog/create', BlogCreate.as_view(), name="blog_create"),
    path('blog/<int:pk>/update', BlogUpdate.as_view(), name="blog_update"),
    path('blog/<int:pk>/delete', BlogDelete.as_view(), name="blog_delete"),
    path('blog/login', LogIn.as_view(), name="login"),
    path('blog/logout', LogOut.as_view(), name="logout")
]
