from django.core.cache import cache

from blogs.models import Blog
from config.settings import CACHE_ENABLED


def get_blogs_from_cache():
    if not CACHE_ENABLED:
        return Blog.objects.all()
    key = 'blog_list'
    blogs = cache.get(key)
    if blogs is not None:
        return blogs
    blogs = Blog.objects.all()
    cache.set(key, blogs)
    return blogs
