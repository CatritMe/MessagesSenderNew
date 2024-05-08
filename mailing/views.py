from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config.settings import EMAIL_HOST_USER
from mailing.forms import MailingForm, MailForm, ClientForm
from mailing.models import Client, Mail, Mailing
from mailing.services import send_mailing


def index(request):
    """главная страница"""
    return render(request, 'mailing/index.html')


# CRUD для модели получателя-------------------------------------------------------------------------


class ClientListView(ListView):
    """Список клиентов-получателей"""
    model = Client


class ClientDetailView(DetailView):
    """Информация по конкретному получателю"""
    model = Client


class ClientCreateView(CreateView):
    """Создание нового получателя"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    """Изменение получателя"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    """Удаление получателя"""
    model = Client
    success_url = reverse_lazy('mailing:client_list')

# CRUD для модели письма-сообщения-------------------------------------------------------------------------


class MailListView(ListView):
    model = Mail


class MailDetailView(DetailView):
    """Информация о конкретном сообщении"""
    model = Mail


class MailCreateView(CreateView):
    """Создание нового письма"""
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail_list')

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['author'] = get_object_or_404(User, pk=self.kwargs.get('pk'))
    #     return context_data


class MailUpdateView(UpdateView):
    """Изменение сообщения"""
    model = Mail
    form_class = MailForm

    def get_success_url(self):
        return reverse('mailing:mail_view', args=[self.kwargs.get('pk')])


class MailDeleteView(DeleteView):
    """Удаление сообщения"""
    model = Mail
    success_url = 'mailing:mail_list'


# CRUD для модели рассылок-----------------------------------------------------------------------------

class MailingListView(ListView):
    """Список всех рассылок"""
    model = Mailing


class MailingDetailView(DetailView):
    """Информация о конкретной рассылке"""
    model = Mailing


class MailingCreateView(CreateView):
    """Создание новой рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        """Отправка рассылки"""
        mailing = form.save()
        mailing.status = 'создана'
        mailing.save()
        send_mailing()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    """Изменение рассылки"""
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:mailing_view', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    """Удаление рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
