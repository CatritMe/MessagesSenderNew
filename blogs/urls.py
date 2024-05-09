from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogDetailView

app_name = BlogsConfig.name

urlpatterns = [
    path('blog_view/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
]