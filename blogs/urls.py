from django.urls import path
from django.views.decorators.cache import cache_page

from blogs.apps import BlogsConfig
from blogs.views import BlogDetailView, BlogListView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog_view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog_view'),
]
