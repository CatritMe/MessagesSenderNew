import random

from django.views.generic import DetailView, ListView

from blogs.models import Blog
from blogs.services import get_blogs_from_cache
from mailing.models import Mailing, Client


class BlogDetailView(DetailView):
    """Просмотр конкретной новости"""
    model = Blog

    def get_object(self, queryset=None):
        """Счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    """Просмотр новостей, главная страница"""
    model = Blog
    template_name = 'blogs/home.html'

    def get_queryset(self):
        """Возвращает список блогов из кэша или БД"""
        return get_blogs_from_cache()

    def get_context_data(self, **kwargs):
        """Возвращает:
         mailings_count - количество рассылок;
         active_mailings_count - количество активных рассылок;
         blog_list - три рандомных блога;
         clients_count - количество уникальных получателей"""
        context_data = super().get_context_data(**kwargs)
        context_data['mailings_count'] = Mailing.objects.all().count()
        context_data['active_mailings_count'] = Mailing.objects.filter(status='запущена').count()
        blog_list = list(self.get_queryset())
        random.shuffle(blog_list)
        context_data['blog_list'] = blog_list[:3]
        context_data['clients_count'] = Client.objects.all().count()
        return context_data
