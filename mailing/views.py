from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Client, Mail


def index(request):
    """главная страница"""
    return render(request, 'mailing/index.html')


# CRUD для модели получателя


class ClientListView(ListView):
    """Список клиентов-получателей"""
    model = Client


class ClientDetailView(DetailView):
    """Информация по конкретному получателю"""
    model = Client


class ClientCreateView(CreateView):
    """Создание нового получателя"""
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    """Изменение получателя"""
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    """Удаление получателя"""
    model = Client
    success_url = reverse_lazy('mailing:client_list')

# CRUD для модели письма-сообщения


class MailListView(ListView):
    model = Mail


class MailDetailView(DetailView):
    """Информация о конкретном сообщении"""
    model = Mail


class MailCreateView(CreateView):
    """Создание нового письма"""
    model = Mail
    fields = ('topic', 'text',)
    success_url = reverse_lazy('mailing:mail_list')

    # def get_success_url(self):
    #     return reverse('mailing:mail_view', args=[self.kwargs.get('pk')])

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['author'] = get_object_or_404(User, pk=self.kwargs.get('pk'))
    #     return context_data


class MailUpdateView(UpdateView):
    """Изменение сообщения"""
    model = Mail
    fields = ('topic', 'text',)

    def get_success_url(self):
        return reverse('mailing:mail_view', args=[self.kwargs.get('pk')])


class MailDeleteView(DeleteView):
    """Удаление сообщения"""
    model = Mail
    success_url = 'mailing:mail_list'

    # def get_success_url(self):
    #     return reverse_lazy('users:author_view', kwargs={'pk': self.object.author.pk})